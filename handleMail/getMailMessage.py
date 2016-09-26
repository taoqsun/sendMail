# -*- coding: utf-8 -*-
'''
Created on Sep 22, 2015

@author: sky
'''
import os
import sys
try:
    from vendors.xlrd.xlrd import *
except Exception,e:
    xldDir = os.path.join(os.path.split(os.path.dirname(__file__))[0],'vendors','xlrd')
    os.chmod(xldDir, 0o777 )
    os.chdir(xldDir)
    #安装xlrd模块
    os.system('python setup.py install')
    
class MailMessage(object):
    
    def __init__(self):
        pass
    
    def getMailMessage(self):
        data = open_workbook(os.path.join(os.path.split(os.path.dirname(__file__))[0],'pay.xlsx'))
        table = data.sheets()[0]
        nrows = table.nrows
        ncols = table.ncols
        pepoleList=[]
          
        for i in range(nrows):
            if table.row(i)[2].value != '' :
                payInfo= table.row_values(i)
                emailAddress= table.row(i)[2].value
                pepole=PepoleInfo(emailAddress,payInfo[:])
                pepoleList.append(pepole)
        
        return pepoleList
                
class PepoleInfo(object):
    
    def __init__(self, emailAddress,payInfo=[]):
        self.emailAddress = emailAddress
        self.payInfo = payInfo
        
    def getPayInfoParam(self):
        return self.payInfo[:]
    
    def getEmailAddressParam(self):
        return self.emailAddress
