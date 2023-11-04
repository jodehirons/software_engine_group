import pandas as pd
# 将数据转化为包含字典的列表
class Student():
    
    def __init__(self,a) :
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
                "选课时间" : row['选课时间'],
                "课程名称" : row['课程名称'].replace('\xa0', ' '),
                "学分" : row['学分'],
                "百分成绩":row['百分成绩'],
                "五分成绩":row['五分成绩'],
                "考试类型":row['考试类型'],
                "选修类型":row['选修类型'].replace('\xa0', ' '),
                # 添加其他学生信息字段
            }
            self.student_list.append(student_info)

    # 打印包含学生信息的列表 student_list
    def showAll(self):
        for student in self.student_list:
            print(student)

