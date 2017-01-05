# -*- coding: utf-8 -*-
__author__ = 'lenovo'

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os

def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body,'html','utf-8')
    msg['subject'] = Header('自动化测试报告','utf-8')

    smtp = smtplib.SMTP_SSL(host = 'smtp.qq.com', port = 465)  #将host port 写入connect中 则QQ拦截。只有这一种方法：用ssl 并且写host port在其中，才行
    # smtp.connect()
    smtp.login('3918747@qq.com','hhtuigzhecxvbiaa')
    smtp.sendmail('3918747@qq.com','3918747@qq.com,37043124@qq.com',msg.as_string())
    smtp.quit()
    print('email has been sent out')

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key = lambda fn: os.path.getmtime(test_report + '\\' + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    test_dir = 'D:\\Python-test\\BookTest\\test_case'
    test_report = 'D:\\Python-test\\BookTest\\report'

    discover =  unittest.defaultTestLoader.discover(test_dir,pattern = 'test*.py')
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    filename = test_report + '\\'+  now + ' result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream = fp, title = '测试报告',description = '用例执行情况：')

    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)

    send_mail(new_report)


