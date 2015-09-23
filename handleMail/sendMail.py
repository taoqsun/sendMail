# -*- coding: utf-8 -*-
import smtplib  
from email.mime.text import MIMEText
from getMailMessage import MailMessage
   
mailto_list=["741187338@qq.com"] 
mail_host="smtp.qq.com"  #设置服务器
mail_user="1750999809@qq.com"    #用户名
mail_pass="123456kk"   #口令 
mail_postfix="qq.com"  #发件箱的后缀
  
def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='utf-8')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        s = smtplib.SMTP_SSL("smtp.qq.com",465, timeout=30)  
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, to_list, msg.as_string())  #发送邮件
        s.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False
  
if __name__ == '__main__':
    mailMessage =MailMessage()
    pepoleList= mailMessage.getMailMessage()
    mailto_list=[]
    message="<table&nbspstyle=\"width:100%;\" border=\"1\" bordercolor=\"#000000\" cellpadding=\"2\" cellspacing=\"0\"\>\<tbody><tr><td>"
    message2=" <td>姓名<br /></td><td>工号<br /></td><td>邮箱<br /></td><td>身份证<br /></td><td>基本工资<br /></td><td>绩效工资<br /></td><td>其他应发<br /></td> \
                <td>应发合计<br /></td><td>病事假<br /></td><td>扣罚<br /></td><td>代扣费用<br /></td><td>补缴四金<br /></td><td>社保<br /></td><td>公积金<br /></td><td>个税<br /> \
               </td><td>其他应扣<br /></td><td>应扣合计<br /></td><td>实发收入<br /></td><td>备注<br /></td><td><br /></td></tr>"
    getMessage="姓名  工号&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp \
                                    邮箱 &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp \
                                    身份证 &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp \
                                    基本工资  绩效工资  其他应发  应发合计  病事假  扣罚  代扣费用  补缴四金  社保  公积金  个税  其他应扣  应扣合计  实发收入  备注  "+'<br>'
    for i in range(2,len(pepoleList)):
        mailto_list.append(str(pepoleList[i].getEmailAddressParam()))
        for j in pepoleList[i].getPayInfoParam():
            getMessage=getMessage+str(j)+'&nbsp&nbsp'  
        if send_mail(mailto_list,str(pepoleList[i].getPayInfoParam()[0])+"工资条",getMessage):  
            print "发送成功"  
        else:  
            print "发送失败"
    