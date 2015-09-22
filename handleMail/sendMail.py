# -*- coding: utf-8 -*-
'''
Created on Sep 22, 2015

@author: sky
'''
import smtplib
import getMailMessage
  
from email.mime.text import MIMEText  
_user = "1750999809@qq.com"  
_pwd  = "123456kk"  
_to   = "741187338@qq.com"  
  

msg = MIMEText("test")
msg["Subject"] = "don't panic"  
msg["From"]    = _user  
msg["To"]      = _to  
  
s = smtplib.SMTP_SSL("smtp.qq.com",465, timeout=30)
s.login(_user, _pwd)
s.sendmail(_user, _to, msg.as_string())  
s.close()