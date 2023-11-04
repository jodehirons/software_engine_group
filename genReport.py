import pandas as pd

# 读取成绩表文件
a = "成绩表.xlsx"
# 在运行前需要再同目录下放置好文件

# 将数据转化为包含字典的列表
class Student():

    def __init__(self, a):
        self.a = a
        self.student_list = []
        self.readExcel()

    def readExcel(self):

        # 读取Excel文件
        data = pd.read_excel(self.a, skiprows=1)

        for index, row in data.iterrows():
            student_info = {
                '学号': row['学号'],
                '姓名': row['姓名'],
                "选课时间": row['选课时间'],
                "课程名称": row['课程名称'].replace('\xa0', ' '),
                "学分": row['学分'],
                "百分成绩": row['百分成绩'],
                "五分成绩": row['五分成绩'],
                "考试类型": row['考试类型'],
                "选修类型": row['选修类型'].replace('\xa0', ' '),
                # 添加其他学生信息字段
            }
            self.student_list.append(student_info)

    # 打印包含学生信息的列表 student_list
    def showAll(self):
        for student in self.student_list:
            print(student)


# 遍历每个学生
for student in self.student_list:
    # 生成成绩信息
    grade_info = ' '.join(f'[{subject}]： {grade}' for subject, grade in zip(subjects, grades))

    # 生成成绩单通知
    notification = f"""
    亲爱的{'姓名'}同学:
    祝贺您顺利完成本学期的学习！教务处在此向您发送最新的成绩单。
    {grade_info} # 需要修改grade_info格式
    希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。如果您在某些科目上没有达到预期的成绩，不要灰心，这也是学习过程中的一部分。我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。
    再次恭喜您，祝您学习进步、事业成功！
    教务处
    """

    # 打印成绩单通知
if __name__ == '__main__':
    student = Student(a)
    print(notification)