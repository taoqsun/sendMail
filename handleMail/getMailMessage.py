# -*- coding: utf-8 -*-
'''
Created on Sep 22, 2015

@author: sky
'''
import os
import sys

try:
    import xlrd
except Exception,e:
    print os.path.split(os.path.dirname(__file__))[0]+'\\vendors\\xlrd-0.9.4&&python setup.py install'
    os.system("cd /d "+os.path.split(os.path.dirname(__file__))[0]+'\\vendors\\xlrd-0.9.4&&python setup.py install')
    
class MailMessage(object):
    
    def __init__(self):
        pass
    
    def getMailMessage(self):
        data = xlrd.open_workbook('../vendors/pay.xlsx')
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


# test=MailMessage()
# print test.getMailMessage()[0].getPayInfoParam()