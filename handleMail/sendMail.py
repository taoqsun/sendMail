# -*- coding: utf-8 -*-
import smtplib  
from email.mime.text import MIMEText
from getMailMessage import MailMessage
import HTMLParser
from __builtin__ import str
import os
import time
   
mail_host="smtp.qq.com"
mail_user="1750999809@qq.com"    #用户名
mail_pass="123456kk"   #口令 
mail_postfix="qq.com"  #发件箱的后缀
  
def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    me="william sun"+"<"+mail_user+"@"+mail_postfix+">"   #这里的william sun可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='utf-8')
    msg['Subject'] = sub    #设置主题
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        s = smtplib.SMTP_SSL("smtp.qq.com",465, timeout=30)  
        s.login(mail_user,mail_pass)  
        s.sendmail(me, to_list, msg.as_string())  
        s.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False
    
def fdbg(log):
        path = os.path.dirname(__file__)
        index = path.rfind("handleMail")
        if(-1 != index):
            logpath = path[:index] + ".\Logs" 
            if(os.path.exists(logpath) == False):
                os.mkdir(logpath)
        else:
            print "Invalid Log file Path."
            return
            
        logfile = logpath + "/" + time.strftime('%Y-%m-%d',time.localtime(time.time())) + ".txt"
        file_handle = open(logfile,"a+")
        file_handle.writelines(str(log) + "\n")
        file_handle.close()
  
def main():
    mailMessage =MailMessage()
    pepoleList= mailMessage.getMailMessage()
    totalMail=len(pepoleList)-2
    mailto_list=[]
    def generate_tr(name, number,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10,number11,number12,number13,number14,number15,number16,number17):
        return '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' %(name, number,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10,number11,number12,number13,number14,number15,number16,number17)
    tds = []
    monthCurr = str(int( time.strftime('%m',time.localtime(time.time())))-1)
    test2= '<table style="width:100%;" border="1" bordercolor="#000000" cellpadding="2" cellspacing="0">'
    test3= '<tr><th>姓名</th><th>工号</th><th>邮箱</th><th>身份证</th><th>基本工资</th><th>绩效工资</th><th>其他应发</th><th>应发合计</th><th>病事假</th><th>扣罚</th><th>代扣费用</th><th>补缴四金</th><th>社保</th><th>公积金</th><th>个税</th><th>其他应扣 </th><th>应扣合计 </th><th>实发收入  </th><th>备注 </th><tr>'
    test5= '</table>'
    
    sendSuccess=0
    sendFail=0
    sendFailInfo=[]
    failInfo=''
    for i in range(2,len(pepoleList)):
        mailto_list.append(str(pepoleList[i].getEmailAddressParam()))
        j =pepoleList[i].getPayInfoParam()
        test4=generate_tr(str(j[0]),str(j[1]),str(j[2]),str(j[3]),str(j[4]),str(j[5]),str(j[6]),str(j[7]),str(j[8]),str(j[9]),str(j[10]),str(j[11]),str(j[12]),str(j[13]),str(j[14]),str(j[15]),str(j[16]),str(j[17]),str(j[18]))
        test1=str(pepoleList[i].getPayInfoParam()[0])+",你好："+"<br/>"+"&nbsp;&nbsp;&nbsp;"+monthCurr+"月工资清单如下，请查阅："+"<br/>"
        if send_mail(mailto_list,str(pepoleList[i].getPayInfoParam()[0])+monthCurr+"月工资条",test1+test2+test3+test4+test5):  
            print "发送成功"
            sendSuccess=sendSuccess+1
        else:  
            print "发送失败"
            sendFail=sendFail+1
            sendFailInfo.append(str(j[0])+','+str(j[1])+','+str(pepoleList[i].getEmailAddressParam()))
        mailto_list=[]
    failInfo="\n".join(sendFailInfo)
    fdbg("total number to send mail:"+str(totalMail)+"\n"+"send success:"+str(sendSuccess)+"\n"+"send fail:"+str(sendFail)+"\n"+"fail information："+"\n"+failInfo)