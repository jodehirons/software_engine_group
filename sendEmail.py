#导入模板库
from docxtpl import DocxTemplate
import pandas as pd
#导入邮件库
import zmail
import time

def sendEmail(mail,sum):

    for i in range(sum):
        #设置收件邮箱
        youXiang=input('请输入第'+str(i+1)+'个收件人邮箱：')

        #设置发件邮箱
        server = zmail.server('2438138449@qq.com','lsatdosepicgdihh')
        #发送邮件
        server.send_mail(youXiang,mail)
        time.sleep(2)
        print('第'+str(i+1)+'封邮件己发送成功')
    print('邮件己全部发送成功')

if __name__ == '__main__':
    # #设置邮件主题
    subject='录取通知书'
    # #设置邮件内容
    content='你己被我校录取，请妥善保管通知书，并按时报到！'

    # #设置邮件信息
    email={'subject':subject,'content_text':content}
    sendEmail(email,2)

