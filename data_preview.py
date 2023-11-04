import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
import pandas as pd
import demo

class window:
    def __init__(self):

        #构建GUI界面
        self.root = Tk()
        self.root.title('成绩预览')
        self.root.geometry('1200x750')
        self.root.config(background='gray')

        #设置内容
        frame = Frame(self.root,borderwidth=5,relief=GROOVE)
        frame.config(background='gray')
        frame.place(x=2, y=65, width=1200, height=650)
        scrollBar = Scrollbar(frame)
        scrollBar.pack(side=RIGHT, fill=Y)
        self.tree = Treeview(frame, columns=('选课时间', '学号', '姓名', '课程名称', '学分','百分成绩','五分成绩','考试类型','选修类型'), show="headings", yscrollcommand=scrollBar.set)
        self.tree.column('选课时间',width=100,anchor='center')
        self.tree.column('学号', width=100, anchor='center')
        self.tree.column('姓名', width=100, anchor='center')
        self.tree.column('课程名称', width=200, anchor='center')
        self.tree.column('学分', width=100, anchor='center')
        self.tree.column('百分成绩', width=100, anchor='center')
        self.tree.column('五分成绩', width=100, anchor='center')
        self.tree.column('考试类型', width=100, anchor='center')
        self.tree.column('选修类型', width=200, anchor='center')

        self.tree.heading('选课时间', text='选课时间')
        self.tree.heading('学号', text='学号')
        self.tree.heading('姓名', text='姓名')
        self.tree.heading('课程名称', text='课程名称')
        self.tree.heading('学分', text='学分')
        self.tree.heading('百分成绩', text='百分成绩')
        self.tree.heading('五分成绩', text='五分成绩')
        self.tree.heading('考试类型', text='考试类型')
        self.tree.heading('选修类型', text='选修类型')

        self.tree.pack(side=LEFT, fill=Y)
        scrollBar.config(command=self.tree.yview)

        self.data = pd.read_excel('成绩表.xlsx')


        frame1 = Frame(self.root, borderwidth=5, relief=GROOVE)
        frame1.place(x=300, y=15, width=580, height=43)
        self.label = Label(frame1, text="输入关键字：")
        self.label.grid(row=4, column=0)
        self.entry = Entry(frame1, width=37)
        self.entry.config(background='Light Blue')
        self.entry.grid(row=4, column=1)
        self.button = Button(frame1, text="查询", anchor='center', command=self.search)
        self.button.grid(row=4, column=4)
        self.var = StringVar()
        self.var.set('所有')
        self.m = ['所有','学号','姓名']

        self.menu = ttk.OptionMenu(frame1, self.var, '', *self.m)
        self.menu.grid(row=4, column=2)

        #使界面一直运行着
        self.root.mainloop()

    def search(self):
        self.tree.delete(*self.tree.get_children())
        if self.var.get() == '所有':
            t = 0
            for index, row in self.data.iterrows():
                t += 1
                if t > 2:
                    self.tree.insert('', 'end',values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        elif self.var.get() == '学号':
            key = self.entry.get()
            t = 0
            for index, row in self.data.iterrows():
                t += 1
                if t > 2 and key in str(row[1]):
                    self.tree.insert('', 'end',values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        elif self.var.get() == '姓名':
            key = self.entry.get()
            t = 0
            for index, row in self.data.iterrows():
                t += 1
                if t > 2 and key in row[2]:
                    self.tree.insert('', 'end',values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))



class notice:
    def __init__(self, value):
        # 构建GUI界面
        self.root = Tk()
        self.root.title('通知预览')
        self.root.geometry('600x400')
        self.root.config(background='gray')

        frame = Frame(self.root, borderwidth=5, relief=GROOVE)
        frame.config(background='gray')
        frame.place(x=10, y=10, width=590, height=390)
        scrollBar = Scrollbar(frame)
        scrollBar.pack(side=RIGHT, fill=Y)

        self.text = Text(frame, height=390)
        self.text.pack()
        self.text.insert(tkinter.END, value)

        self.root.mainloop()


