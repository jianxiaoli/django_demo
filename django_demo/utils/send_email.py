#!/usr/bin/python
# -*- coding: UTF-8 -*

__author__ = 'Schuyang'
__version__ = ''
__all__ = []

# 标准库

# 第三方库

# 自定义库

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
# mail_host = '192.169.0.125'
mail_user = "475714446@qq.com"  # 用户名
mail_pass = "fruheksvdolcbgda"  # 口令
sender = '475714446@qq.com'
receivers = ['xuliang@atomdatatech.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header(sender, 'utf-8')
message['To'] = Header('xuliang@atomdatatech.com', 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    # smtpObj = smtplib.SMTP()
    # smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    # smtpObj.login(mail_user, mail_pass)
    # smtpObj.sendmail(sender, receivers, message.as_string())
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header(sender, 'utf-8')
    message['To'] = Header('xuliang@atomdatatech.com', 'utf-8')
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('Python 邮件发送测试……', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(r'D:\codespace\calc_service\test.csv', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="test.csv"'
    message.attach(att1)

    # 构造附件2，传送当前目录下的 runoob.txt 文件
    # att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
    # message.attach(att2)

    # 使用qq邮箱发送
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(mail_user, mail_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
    server.quit()  # 关闭连接
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件")

