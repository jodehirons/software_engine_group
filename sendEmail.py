#导入模板库
import pandas as pd
#导入邮件库
import zmail
import time

def sendEmail(email,mail):
    #设置发件邮箱
    server = zmail.server('2438138449@qq.com','lsatdosepicgdihh')
    #发送邮件
    server.send_mail(mail ,email)
    time.sleep(2)
    print('邮件己发送成功')
    print('邮件己全部发送成功')

def sendMain(notification,mail):
    # #设置邮件主题
    subject='成绩通知单'
    print(notification,subject)
    # #设置邮件内容
    for i in notification:
        print(i)
        content=i
        # #设置邮件信息
        email={'subject':subject,'content_text':content}
        sendEmail(email,mail)

