import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import dataPreview
import getEmailInformation

# 创建主窗口
root = TkinterDnD.Tk()
root.title("自动发送学生通知邮件")
root.geometry("300x300")  # 设置窗口大小

# 存储文件路径的变量
path = ""

# 存储邮箱地址的变量
mail = ""
# 函数：拖拽文件后的处理
def drop(event):
    global path
    path = event.data
    open_success_window("读取成功")

# 函数：打开新窗口来显示成功信息
def open_success_window(message):
    success_window = tk.Toplevel()
    success_window.title("操作成功")
    success_label = tk.Label(success_window, text=message, padx=20, pady=10)
    success_label.pack()
    success_window.after(2000, success_window.destroy)

# 函数：确定邮箱地址
def set_email():
    global mail
    mail = mail_entry.get()
    if mail == "":
        open_success_window("邮箱地址不能为空")
    else:
        open_success_window("邮箱地址设置成功")

# 函数：预览成绩
def preview_score():
    if path:
        f = dataPreview.window(path)
    else:
        open_success_window("请先拖拽文件")

# 函数：预览通知
def preview_announce():
    if path:
        getEmailInformation.main(path)
    else:
        open_success_window("请先拖拽文件")

# 函数：发送通知
def send_mail():
    if path and mail:
        getEmailInformation.sendMail(path, mail)
        open_success_window("发送通知完成")
    else:
        open_success_window("请先拖拽文件和输入邮箱地址")

# 添加标题
title_label = tk.Label(root, text="自动发送学生通知邮件", font=("Tahoma", 18))
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# 创建拖拽区域
drop_label = tk.Label(root, text="拖拽文件至此", width=30, height=5)
drop_label.grid(row=1, column=0, pady=10, columnspan=3)  # 使用grid布局
drop_label.drop_target_register(DND_FILES)
drop_label.dnd_bind('<<Drop>>', drop)

# 创建邮箱输入框
mail_label = tk.Label(root, text="接收人:")
mail_label.grid(row=2, column=0, padx=5)
mail_entry = tk.Entry(root)
mail_entry.grid(row=2, column=1)
email_button = tk.Button(root, text="确定", command=set_email)
email_button.grid(row=2, column=2)
email_status_label = tk.Label(root, text="")
email_status_label.grid(row=3, column=0, columnspan=3)

# 创建按钮
score_button = tk.Button(root, text="预览成绩", command=preview_score)
score_button.grid(row=4, column=0, padx=5)

announce_button = tk.Button(root, text="预览通知", command=preview_announce)
announce_button.grid(row=4, column=1, padx=5)

send_button = tk.Button(root, text="发送通知", command=send_mail)
send_button.grid(row=4, column=2, padx=5)

# 创建状态标签
status_label = tk.Label(root, text="")
status_label.grid(row=5, column=0, columnspan=3)

root.mainloop()
