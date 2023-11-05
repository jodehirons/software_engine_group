import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD

def on_drop(event):
    file_path = event.data
    file_label.config(text=f"File Path: {file_path}")

root = TkinterDnD.Tk()
root.title("文件拖放示例")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

file_label = tk.Label(frame, text="拖放文件到这里")
file_label.pack(padx=10, pady=10)

file_label.drop_target_register(DND_FILES)
file_label.dnd_bind('<<Drop>>', on_drop)

root.mainloop()
