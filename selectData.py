import tkinter as tk
from tkinter import ttk  # 导入ttk模块用于改进界面外观
from readExcel import Student

class window:
    def __init__(self,path):
        self.dataSelect = []
        self.path = path

    def getWindow(self):
        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("数据显示应用")

        # 设置窗口大小
        self.root.geometry("600x400")

        # 创建一个框架，用于包装列表框和滚动条
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.student = Student(self.path)

        # 获取学号数据
        data = []
        for datas in self.student.student_list:
            student_id_value = datas.get('学号')
            student_name_value = datas.get('姓名')
            data.append([student_id_value, student_name_value])

        data1 = data
        data = []
        for item in data1:
            if item not in data:
                data.append(item)

        # 创建一个 Listbox，用于显示学号数据
        self.data_listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE)
        for item in data:
            self.data_listbox.insert(tk.END, item)
        self.data_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 创建一个滚动条并将其关联到 Listbox
        scrollbar = tk.Scrollbar(frame, command=self.data_listbox.yview)
        self.data_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 创建一个按钮，点击时调用 get_selected_items 函数
        get_button = tk.Button(self.root, text="确定", command=self.get_selected_items)
        get_button.pack(pady=10)
        self.root.mainloop()

        # 创建一个函数，用于获取所选项目

    def getData(self):
        return self.dataSelect
    def get_selected_items(self):
        selected_indices = self.data_listbox.curselection()
        selected_items = [self.data_listbox.get(index) for index in selected_indices]
        student_ids = [item[0] for item in selected_items]
        for datas in self.student.student_list:
            student_id_value = datas.get('学号')
            if student_id_value in student_ids:
                self.dataSelect.append(datas)
        # print("所选学号：", selected_items)
        # print("所选学号学生信息：", dataSelect)
        self.root.destroy()
        self.root.quit()
        # email = EmailInformation(self.dataSelect)
        # email.generateNotification()
        # notification = email.generateNotification()
        # for notification in notification:
        #     print(notification)

        # 启动主循环


#
# f = window('../成绩表.xlsx')
# f.getWindow()
# print(f.dataSelect)

#### "所选学号学生信息：", dataSelect列表中的数据格式如下：[{...},{...},{...}]