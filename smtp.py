#/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header
import smtplib

def format_addr(addr):
    name, addr = parseaddr(addr)
    return formataddr((Header(name, 'utf-8').encode(), addr))




from_addr = '18701994373@163.com' #input('From: ')
passwd = 'aiying1007'#input("Password: ")
to_addr = '103664210@qq.com'#input('To: ')

msg = MIMEMultipart()
msg['From'] = format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自python的问候...', 'utf-8').encode()
text = MIMEText('send with file... haha', 'plain', 'utf-8')
encoders.encode_base64(text)
msg.attach(text)

with open('/Volumes/mac/IMG_0295.JPG', 'rb') as image:
    mime = MIMEBase('image', 'jpg', filename='IMG_0295.JPG')
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(image.read())
    encoders.encode_base64(mime)
    msg.attach(mime)


smtp_server = 'smtp.163.com'#input('SMTP server: ')


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, passwd)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
