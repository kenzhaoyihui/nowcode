# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.header import Header
from email import encoders
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#msg = MIMEText('Hello, send by python3...', 'plain', 'utf-8')

from_addr = input('From: ')
#password = input('Password: ')

to_addr = input('To: ')

smtp_server = input('SMTP server: ')

msg = MIMEMultipart()
#msg = MIMEText('Hello, LittleSisterFairy LJ...', 'plain', 'utf-8')
#msg = MIMEText('<html><body><h1>Hello</h1>' +
    #'<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    #'</body></html>', 'html', 'utf-8')
msg['From'] = _format_addr('Yihui Zhao <%s>' % from_addr)
#msg['From'] = "Chouzhu"
msg['To'] = _format_addr('You are so smart--<%s>' % to_addr)
msg['Subject'] = Header("From hyz' love...", 'utf-8').encode()

#msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
#msg.attach(MIMEText('LJ, I Love You...', 'html', 'utf-8'))

msg.attach(MIMEText('<html><body><h1>Mosherry_LJ</h1>' + '<p><img src="cid:0"></p>' + '</body></html>', 'html', 'utf-8'))

with open("desktop.jpg", 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename='lj.jpg')
    mime.add_header('Content-Disposition', 'attachment', filename='lj.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # add the content from attachment
    mime.set_payload(f.read())
    # use base64 encode
    encoders.encode_base64(mime)
    # add to MIMEMultipart
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.starttls()
server.set_debuglevel(1)
#server.login(from_addr)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()