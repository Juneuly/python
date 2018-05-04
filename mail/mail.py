#coding:utf-8

from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(),addr))


from_addr = 'wangsx0@163.com'
passwd = '****'
to_addr = 'juneuly1@163.com'
smtp_server = 'smtp.163.com'

msg = MIMEText('下午两点来开会!', 'plain', 'utf-8')
msg['From'] = _format_addr(from_addr)
msg['To'] = _format_addr(to_addr)
msg['Subject'] = Header('开会提醒','utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,passwd)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()

