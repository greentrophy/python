import pyodbc
import tkinter as tk
from tkinter import messagebox

# 连接到数据库
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=HQK;'
    'DATABASE=book1;'
    'Trusted_Connection=yes;'
)

# 创建主界面
root = tk.Tk()

def list_users(event=None):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_login")
    users = cursor.fetchall()
    if users:
        user_info = "已有用户如下：\n"
        for user in users:
            user_info += f"用户名：{user[0]}，密码：{user[1]}\n"
        messagebox.showinfo("已有用户", user_info)
    else:
        messagebox.showerror("错误", "暂无用户！")

def add_user(username, password):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_login (用户名, 密码) VALUES (?, ?)", (username, password))
    conn.commit()
    messagebox.showinfo("提示", "添加用户成功！")

def delete_user(username):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user_login WHERE 用户名=?", (username,))
    conn.commit()
    messagebox.showinfo("提示", "删除用户成功！")

# 创建控件
label1 = tk.Label(root, text="请输入用户名：")
entry1 = tk.Entry(root)

label2 = tk.Label(root, text="请输入密码：")
entry2 = tk.Entry(root)

button1 = tk.Button(root, text="添加用户", command=lambda: add_user(entry1.get(), entry2.get()))

button2 = tk.Button(root, text="删除用户", command=lambda: delete_user(entry1.get()))

button3 = tk.Button(root, text="查看已有用户", command=list_users)

# 布局控件
label1.grid(row=0, column=0, padx=5, pady=5)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2.grid(row=1, column=0, padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)

button1.grid(row=2, column=0, padx=5, pady=5)
button2.grid(row=2, column=1, padx=5, pady=5)

button3.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# 运行主界面
root.mainloop()