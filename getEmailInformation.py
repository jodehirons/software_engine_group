import pandas as pd
import  selectData
import  dataPreview
import sendEmail

data = []
class EmailInformation:
    """
    EmailInformation类用于处理学生的电子邮件信息。
    """
    def __init__(self, student):
        """
        初始化方法，接收一个Student对象作为参数，从该对象中获取学生信息。
        """
        self.student = student
        self.studentIdName = self.generateIdNameMapping()
        self.studentGrades = self.separateGradesById()
        

    def generateIdNameMapping(self):
        '''
        生成学号和姓名的映射
        '''
        studentIdName = {}
        for student in self.student:
            studentIdName[student['学号']] = student['姓名']
        return studentIdName
    
    def separateGradesById(self):
        '''
        将学生的成绩按照学号分开
        '''
        studentGrades = {}
        for student in self.student:
            studentId = student['学号']
            if studentId not in studentGrades:
                studentGrades[studentId] = []
            courseName = ''
            score = 0
            for subject, item in student.items():
                if subject == '课程名称':
                    courseName = item
                if subject == '百分成绩':
                    score = item
            studentGrades[studentId].append((courseName, score))
        return studentGrades
    
    
    def generateNotification(self):
        '''
        生成成绩单通知
        '''
        notificationList = []
        for studentId in self.studentIdName.keys():
            studentName = self.studentIdName[studentId]
            grades = self.studentGrades[studentId]
            subjects = [subject for subject, grade in grades]
            grades = [grade for subject, grade in grades]
            gradeInfo = '\n'
            for subject, grade in zip(subjects, grades):
                gradeInfo += f'[{subject}]： {grade} \n '

            notification = f"""
            亲爱的{studentName}同学:
            祝贺您顺利完成本学期的学习！教务处在此向您发送最新的成绩单:
            {gradeInfo}
            希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。如果您在某些科目上没有达到预期的成绩，不要灰心，这也是学习过程中的一部分。我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。
            """
            notificationList.append(notification)
        return notificationList

def main(path):
    selectData.window(path)
    data = selectData.dataOut()
    emailInformation = EmailInformation(data)
    notification = emailInformation.generateNotification()
    f = dataPreview.notice(notification)

def sendMail(path,mail):
    selectData.window(path)
    data = selectData.dataOut()
    emailInformation = EmailInformation(data)
    notification = emailInformation.generateNotification()
    sendEmail.sendMain(notification,mail)