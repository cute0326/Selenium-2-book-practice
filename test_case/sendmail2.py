#coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtpserver = 'smtp.qq.com'

sender = '3918747@qq.com'

receiver = 'cute0326@qq.com'

user = '3918747@qq.com'
password = 'hhtuigzhecxvbiaa'

subject = 'Python automatically send email with attachment'

sendfile = open('2016-10-24 20-50-26 result.html','rb').read()

# att = MIMEText(sendfile,'base64','utf-8')
#
# att['Content-Type'] = 'applicaton/cotet-stream'
# att['Content-Disposition'] = 'attachment; filename = "2016-10-24 20-50-26 result.html"'

# msgRoot = MIMEMultipart('related')
# msgRoot['subject'] = subject
# # msgRoot.attach(att)

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('related') #改成relative 则附件编程html和bin了 为什么会是bin好奇怪。然后附件名字也是一堆数字，和我猜或者原来的名字没啥关系。
# 测试之后发现是如果附件哪里的名字写汉字，就会出bin文件，写英文就没事儿。att["Content-Disposition"] = 'attachment; filename="也许.jpg"'
msg['Subject'] = "Link"

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\


Hi!

       How are you?

       Here is the <a href="http://www.python.org">link</a> you wanted.



"""
#这段html虽然写成这样，但是显示的时候，除了link没有格式的。
# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
# 即html替代了text，试过把html的注销掉，那么邮件内容就显示text了。
msg.attach(part1)
msg.attach(part2)
#构造附件
att = MIMEText(open('D:\\Python-test\\BookTest\\result.jpg', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="result.jpg"'
msg.attach(att)

smtp = smtplib.SMTP_SSL(host = 'smtp.qq.com', port = 465)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
