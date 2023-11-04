import pandas as pd

# ��ȡ�ɼ����ļ�
df = pd.read_excel('grades.xlsx')

# ��ȡ���п�Ŀ�����ƣ���ȥ'����'��'ѧ��'
subjects = df.columns.drop(['����', 'ѧ��']).tolist()

# ����ÿһ��
for index, row in df.iterrows():
    # ��ȡѧ����Ϣ
    name = row['����']
    id = row['ѧ��']
    
    # ��ȡ���п�Ŀ�ĳɼ�
    grades = [row[subject] for subject in subjects]  # �����ʵ������޸�
    
    
    # ���ɳɼ���Ϣ
    grade_info = ' '.join(f'[{subject}]�� {grade}' for subject, grade in zip(subjects, grades))

    # ���ɳɼ���֪ͨ
    notification = f"""
    �װ���{name}ͬѧ:
    ף����˳����ɱ�ѧ�ڵ�ѧϰ�������ڴ������������µĳɼ�����
    {grade_info}
    ϣ�����ܹ����Լ��ĳɼ��е����⣬����������Ŭ���ͻ�����ѧϰ̬�ȡ��������ĳЩ��Ŀ��û�дﵽԤ�ڵĳɼ�����Ҫ���ģ���Ҳ��ѧϰ�����е�һ���֡����ǹ������������ον�ʦ�򸨵�Ա���н��������ǽ�������Ϊ������κ����ʲ��ṩ���������ס��ѧϰ��һ���������ϵĹ��̣������������������˷����Ѳ�ȡ�ø���Ľ�����
    �ٴι�ϲ����ף��ѧϰ��������ҵ�ɹ���
    ����
    """

    # ��ӡ�ɼ���֪ͨ
    print(notification)