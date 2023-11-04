import pandas as pd

# ��ȡ�ɼ����ļ�
a = "�ɼ���.xlsx"
# ������ǰ��Ҫ��ͬĿ¼�·��ú��ļ�

# ������ת��Ϊ�����ֵ���б�
class Student():

    def __init__(self, a):
        self.a = a
        self.student_list = []
        self.readExcel()

    def readExcel(self):

        # ��ȡExcel�ļ�
        data = pd.read_excel(self.a, skiprows=1)

        for index, row in data.iterrows():
            student_info = {
                'ѧ��': row['ѧ��'],
                '����': row['����'],
                "ѡ��ʱ��": row['ѡ��ʱ��'],
                "�γ�����": row['�γ�����'].replace('\xa0', ' '),
                "ѧ��": row['ѧ��'],
                "�ٷֳɼ�": row['�ٷֳɼ�'],
                "��ֳɼ�": row['��ֳɼ�'],
                "��������": row['��������'],
                "ѡ������": row['ѡ������'].replace('\xa0', ' '),
                # �������ѧ����Ϣ�ֶ�
            }
            self.student_list.append(student_info)

    # ��ӡ����ѧ����Ϣ���б� student_list
    def showAll(self):
        for student in self.student_list:
            print(student)


# ����ÿ��ѧ��
for student in self.student_list:
    # ���ɳɼ���Ϣ
    grade_info = ' '.join(f'[{subject}]�� {grade}' for subject, grade in zip(subjects, grades))

    # ���ɳɼ���֪ͨ
    notification = f"""
    �װ���{'����'}ͬѧ:
    ף����˳����ɱ�ѧ�ڵ�ѧϰ�������ڴ������������µĳɼ�����
    {grade_info} # ��Ҫ�޸�grade_info��ʽ
    ϣ�����ܹ����Լ��ĳɼ��е����⣬����������Ŭ���ͻ�����ѧϰ̬�ȡ��������ĳЩ��Ŀ��û�дﵽԤ�ڵĳɼ�����Ҫ���ģ���Ҳ��ѧϰ�����е�һ���֡����ǹ������������ον�ʦ�򸨵�Ա���н��������ǽ�������Ϊ������κ����ʲ��ṩ���������ס��ѧϰ��һ���������ϵĹ��̣������������������˷����Ѳ�ȡ�ø���Ľ�����
    �ٴι�ϲ����ף��ѧϰ��������ҵ�ɹ���
    ����
    """

    # ��ӡ�ɼ���֪ͨ
if __name__ == '__main__':
    student = Student(a)
    print(notification)