# -*- coding: utf-8 -*-
# @Time    : 2018/9/9 6:24 PM
# @Author  : Zhixin Piao 
# @Email   : piaozhx@shanghaitech.edu.cn

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from config import mail_host, mail_user, mail_pass

sender = 'piaozhx@shanghaitech.edu.cn'
receivers = ['piaozhx@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 587)  # 25 为 SMTP 端口号

    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.ehlo()

    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")

except smtplib.SMTPException:
    print("Error: 无法发送邮件")
