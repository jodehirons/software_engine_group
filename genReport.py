import pandas as pd
import dataPreview
import sendEmail
import readExcel
# 将数据转化为包含字典的列表
class Student():

    def __init__(self, a, mail):
        self.a = a
        self.mail = mail
        self.student_list = []
    def generateNotice(self):

        # 读取Excel文件

        sendEmail.sendMain(notification,self.mail)

    def readOnce(self):
        data = pd.read_excel(self.a)
        t = 0
        for index, row in data.iterrows():
            t += 1
            if t == 3:
                notification = "亲爱的" + str(row[
                                                  2]) + "同学:\n" + "  祝贺您顺利完成本学期的学习！\n" + "  教务处在此向您发送最新的成绩单。" + '希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。如果您在某些科目上没有达到预期的成绩，不要灰心，这也是学习过程中的一部分。我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。\n' + '  再次恭喜您，祝您学习进步、事业成功！\n' + '  教务处'

                return notification

# 获取第一个成绩单通知
def getNotice(path,mail):
    student = Student(path , mail)
    dataPreview.notice(student.readOnce())

# 生成成绩单通知
def generateMail(path,mail):
    student = Student(path , mail)
    student.generateNotice()
