'''
SMTP发送邮件
smtp是发送邮件的协议，内置对协议的支持，可以发送纯文本邮件，html邮件和带附件的邮件
python对smtp支持有smtplib和email两个模块。
email负责构造邮件，smtplib负责发送邮件

'''
# #构造一个简单的纯文本邮件
# from email.mime.text import MIMEText
# msg=MIMEText('hello,send by py ','plain','utf-8')
# #注意到构造MIMEText对象时，第一个参数就是邮件正文，
# #第二个参数是subtype，‘plain’表示纯文本
#
# #然后通过SMTP发出去
#
# #输入email地址和口令
# from_addr=input('From:')
# password=input('password:')
# #输入收件人地址
# to_addr=input('to:')
# #输入SMTP服务器地址
# smtp_server=input('SMTP server:')
#
# import smtplib
# server=smtplib.SMTP(smtp_server,25)
# #协议默认端口是25
# server.set_debuglevel(1)#打印出服务器交互的所有信息
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()
#--------------------------------------------------

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'zhuangfifi1996@163.com'
password = input('Password: ')
to_addr = '747548958@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

'''
小结
使用Python的smtplib发送邮件十分简单，
只要掌握了各种邮件类型的构造方法，正确设置好邮件头，就可以顺利发出
构造一个邮件对象就是一个Messag对象
如果构造一个MIMEText对象,就表示一个文本邮件对象
如果构造一个MIMEImage对象,就表示一个作为附件的图片
要把多个对象组合起来,就用MIMEMultipart对象，
而MIMEBase可以表示任何对象
它们的继承关系如下：
Message
+- MIMEBase
   +- MIMEMultipart
   +- MIMENonMultipart
      +- MIMEMessage
      +- MIMEText
      +- MIMEImage
'''