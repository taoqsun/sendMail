# -*- coding: utf-8 -*-
import smtplib  
from email.mime.text import MIMEText
from getMailMessage import MailMessage
import HTMLParser
from __builtin__ import str
import os
import time
   
mail_host="smtp.sina.com"
mail_user="fuyao_hr"    #用户名
mail_pass=""   #口令 
mail_postfix="sina.com"  #发件箱的后缀

# mail_host="smtp.qq.com"
# mail_user="1750999809@qq.com"    #用户名
# mail_pass=""   #口令 
# mail_postfix="qq.com"  #发件箱的后缀
  
def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    titleMessage=str("富爻HR".decode("utf-8").encode("gb2312"))
    me=titleMessage+"<"+mail_user+"@"+mail_postfix+">"   #这里的william sun可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='utf-8')
    msg['Subject'] = sub    #设置主题
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        s = smtplib.SMTP_SSL("smtp.sina.com",465, timeout=30)
#         s = smtplib.SMTP_SSL("smtp.qq.com",465, timeout=30)  
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
        return '<tr><td>{0:s}</td><td>{1:d}</td><td>{2:s}</td><td>{3:s}</td><td>{4:10.2f}</td><td>{5:10.2f}</td><td>{6:10.2f}</td><td>{7:10.2f}</td><td>{8:10.2f}</td><td>{9:10.2f}</td><td>{10:10.2f}</td><td>{11:10.2f}</td><td>{12:10.2f}</td><td>{13:10.2f}</td><td>{14:10.2f}</td><td>{15:10.2f}</td><td>{16:10.2f}</td><td>{17:10.2f}</td><td>{18:s}</td></tr>'.format(name, number,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10,number11,number12,number13,number14,number15,number16,number17)
#         return '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' %(name, number,number1,number2,number3,number4,number5,number6,number7,number8,number9,number10,number11,number12,number13,number14,number15,number16,number17)
    tds = []
    monthCurr = str(int( time.strftime('%m',time.localtime(time.time())))-1)
    test2= '<table style="width:100%;" border="1" bordercolor="#000000" cellpadding="2" cellspacing="0">'
    test3= '<tr><th>姓名</th><th>工号</th><th>邮箱</th><th>身份证</th><th>基本工资</th><th>绩效工资</th><th>其他应发</th><th>应发合计</th><th>病事假</th><th>扣罚</th><th>代扣费用</th><th>补缴四金</th><th>社保</th><th>公积金</th><th>个税</th><th>其他应扣 </th><th>应扣合计 </th><th>实发收入  </th><th>备注 </th><tr>'
    test5= '</table>'
    test6= '<br/>'+'[郑重提示]'+'<br/>'+'1、 请妥善保管此薪资清单；'+'<br/>'+'2、 薪资属于保密信息，未经授权、许可不得以任何理由向外界透漏自己的薪资信息，也不得以任何理由询问或了解他人的薪资信息； 如因个人原因导致薪资信息泄露，公司将会追究相关责任并进行处罚。'+'<br/>'+'（如有疑问，请联系人事行政部，及时给您回复！）'
    sendSuccess=0
    sendFail=0
    sendFailInfo=[]
    failInfo=''
    
    for i in range(2,len(pepoleList)):
        mailto_list.append(str(pepoleList[i].getEmailAddressParam().strip()))
        test7=str("月工资条".decode("utf-8").encode("gb2312"))
        subMessage=monthCurr+test7
        j =pepoleList[i].getPayInfoParam()
        test4=generate_tr(str(j[0].encode("utf-8")),int(j[1]),str(j[2]),str(j[3]),float(j[4]),float(j[5]),float(j[6]),float(j[7]),float(j[8]),float(j[9]),float(j[10]),float(j[11]),float(j[12]),float(j[13]),float(j[14]),float(j[15]),float(j[16]),float(j[17]),str(j[18].encode("utf-8")))
        test1=str(pepoleList[i].getPayInfoParam()[0].encode("utf-8"))+",你好："+"<br/>"+"&nbsp;&nbsp;&nbsp;"+monthCurr+"月工资清单如下，请查阅："+"<br/>"
        if send_mail(mailto_list,subMessage,test1+test2+test3+test4+test5+test6):  
            print "发送成功"
            sendSuccess=sendSuccess+1
        else:  
            print "发送失败"
            sendFail=sendFail+1
            sendFailInfo.append(str(j[0].encode("utf-8"))+','+str(j[1])+','+str(pepoleList[i].getEmailAddressParam()))
        mailto_list=[]
        time.sleep(20)
    failInfo="\n".join(sendFailInfo)
    fdbg("total number to send mail:"+str(totalMail)+"\n"+"send success:"+str(sendSuccess)+"\n"+"send fail:"+str(sendFail)+"\n"+"fail information："+"\n"+failInfo)