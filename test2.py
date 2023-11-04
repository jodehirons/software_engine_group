import tkinter as tk
from tkinter import ttk  # 导入ttk模块用于改进界面外观
from test import Student

# 创建主窗口
root = tk.Tk()
root.title("数据显示应用")

# 设置窗口大小
root.geometry("600x400")

# 创建一个框架，用于包装列表框和滚动条
frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

student = Student("成绩表.xlsx")

# 获取学号数据
data = []
for datas in student.student_list:
    student_id_value = datas.get('学号')
    student_name_value = datas.get('姓名')
    data.append([student_id_value, student_name_value])

data1 = data
data = []
for item in data1:
    if item not in data:
        data.append(item)

# 创建一个 Listbox，用于显示学号数据
data_listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE)
for item in data:
    data_listbox.insert(tk.END, item)
data_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 创建一个滚动条并将其关联到 Listbox
scrollbar = tk.Scrollbar(frame, command=data_listbox.yview)
data_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 创建一个函数，用于获取所选项目
dataSelect = []
def get_selected_items():
    selected_indices = data_listbox.curselection()
    selected_items = [data_listbox.get(index) for index in selected_indices]
    student_ids = [item[0] for item in selected_items]
    for datas in student.student_list:
        student_id_value = datas.get('学号')
        if student_id_value in student_ids:
            dataSelect.append(datas)
    print("所选学号：", selected_items)
    print("所选学号学生信息：", dataSelect)

# 创建一个按钮，点击时调用 get_selected_items 函数
get_button = tk.Button(root, text="确定", command=get_selected_items)
get_button.pack(pady=10)

# 启动主循环
root.mainloop()



#### "所选学号学生信息：", dataSelect列表中的数据格式如下：[{...},{...},{...}]