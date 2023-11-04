import pandas as pd

# 读取成绩表文件
df = pd.read_excel('grades.xlsx')

# 获取所有科目的名称，除去'姓名'和'学号'
subjects = df.columns.drop(['姓名', '学号']).tolist()

# 遍历每一行
for index, row in df.iterrows():
    # 获取学生信息
    name = row['姓名']
    id = row['学号']
    
    # 获取所有科目的成绩
    grades = [row[subject] for subject in subjects]  # 请根据实际情况修改
    
    
    # 生成成绩信息
    grade_info = ' '.join(f'[{subject}]： {grade}' for subject, grade in zip(subjects, grades))

    # 生成成绩单通知
    notification = f"""
    亲爱的{name}同学:
    祝贺您顺利完成本学期的学习！教务处在此向您发送最新的成绩单。
    {grade_info}
    希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。如果您在某些科目上没有达到预期的成绩，不要灰心，这也是学习过程中的一部分。我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。
    再次恭喜您，祝您学习进步、事业成功！
    教务处
    """

    # 打印成绩单通知
    print(notification)