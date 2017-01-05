# -*- coding: utf-8 -*-
__author__ = 'lenovo'

#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender="Cute.Yang"
to_mail=["3918747@qq.com"]
username="3918747@qq.com"

#QQ授权码
mail_pwd="dfsdpjstwvsybhgg"

filename = '../2016-10-25 13_11_33 result.html'

fo=open(filename,'rb')
html=fo.read()
html=fo.read()
fo.close()


msg=MIMEText(html,"html","utf-8")
msg['To'] =";".join(to_mail)
msg['From']='FanGu<'+username+'>'
msg['Subject']='python send mail'

if __name__ == '__main__':
    smtp=smtplib.SMTP_SSL()
    smtp.connect("smtp.qq.com")
    smtp.login(username, mail_pwd)
    smtp.sendmail(sender,to_mail,msg.as_string())
    smtp.close()