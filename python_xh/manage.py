import tkinter as tk
from tkinter import ttk
import os

# 创建主窗口
root = tk.Tk()
root.title("跳转界面")
root.geometry("400x200")

# 设计并放置标签
label = ttk.Label(root, text="请选择要跳转的界面：", font=("Helvetica", 16))
label.pack(pady=20)

# 设计并放置按钮
btn1 = ttk.Button(root, text="管理图书", command=lambda: os.system("python bookmanage.py"))
btn1.pack(pady=10)
btn2 = ttk.Button(root, text="管理用户", command=lambda: os.system("python usermanage.py"))
btn2.pack(pady=10)

# 运行主循环
root.mainloop()