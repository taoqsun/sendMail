'''
Created on Sep 22, 2015

@author: sky
'''
import smtplib  
from email.mime.text import MIMEText  
_user = "1750999809@qq.com"  
_pwd  = "1314520kk"  
_to   = "741187338@qq.com"  
  
#使用MIMEText构造符合smtp协议的header及body  
msg = MIMEText("乔装打扮，不择手段")  
msg["Subject"] = "don't panic"  
msg["From"]    = _user  
msg["To"]      = _to  
  
s = smtplib.SMTP_SSL("smtp.qq.com",467, timeout=30)#连接smtp邮件服务器,端口默认是25  
s.login(_user, _pwd)#登陆服务器  
s.sendmail(_user, _to, msg.as_string())#发送邮件  
s.close()