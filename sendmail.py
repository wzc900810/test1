#!/usr/bin/env python
# coding:utf8

import smtplib
from email.mime.text import MIMEText
from sys import argv

# mailto_list = []
mail_host = "smtp.163.com:465"  # 设置服务器
mail_user = "82375881@163.com"     # 发件用户名(换成自己的)
mail_pass = "wzc953764182"   # 口令（换成自己的）
# mail_postfix = "163.com"  # 发件箱的后缀
debug_level = 0       # 是否开启debug

def send_mail(to_list, sub, content):
    me = mail_user
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = mailto_list
    try:
        server = smtplib.SMTP_SSL()
        server.set_debuglevel(debug_level)
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    try:
        mailto_list = argv[1]
        sub = argv[2]
        content = argv[3]
    except:
        print "python send_mail.py 'user1@xx.com;user2@xx.com' sub content"
        exit()

    if send_mail(mailto_list, sub, content):
        print "发送成功"
    else:
        print "发送失败"