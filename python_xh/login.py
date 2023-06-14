import pyodbc
import tkinter as tk
from tkinter import messagebox
import os

# 连接到数据库
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=HQK;'
    'DATABASE=book1;'
    'Trusted_Connection=yes;'
)
# 创建游标对象
cursor = conn.cursor()

# 登录界面
class LoginFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        # 增加空白行
        self.grid_rowconfigure(0, minsize=50)
        self.grid_rowconfigure(6, minsize=50)
        # 增加空白列
        self.grid_columnconfigure(0, minsize=50)
        self.grid_columnconfigure(3, minsize=50)
        
        self.type = tk.StringVar(value='1')
        self.lbl_title = tk.Label(self, text='欢迎登录', font=('Arial', 24))
        self.lbl_title.grid(row=2, column=1, columnspan=2, pady=10)
        self.lbl_type = tk.Label(self, text='登录类型：')
        self.lbl_type.grid(row=3, column=1, padx=10, pady=10, sticky=tk.E)
        self.rad_user = tk.Radiobutton(self, text='用户登录', variable=self.type, value='1')
        self.rad_user.grid(row=3, column=2, padx=10, pady=10, sticky=tk.W)
        self.rad_admin = tk.Radiobutton(self, text='管理员登录', variable=self.type, value='2')
        self.rad_admin.grid(row=4, column=2, padx=10, pady=10, sticky=tk.W)
        self.lbl_username = tk.Label(self, text='用户名：')
        self.lbl_username.grid(row=5, column=1, padx=10, pady=10, sticky=tk.E)
        self.ent_username = tk.Entry(self)
        self.ent_username.grid(row=5, column=2, padx=10, pady=10, sticky=tk.W)
        self.lbl_password = tk.Label(self, text='密码：')
        self.lbl_password.grid(row=6, column=1, padx=10, pady=10, sticky=tk.E)
        self.ent_password = tk.Entry(self, show='\u2022')
        self.ent_password.grid(row=6, column=2, padx=10, pady=10, sticky=tk.W)
        self.btn_login = tk.Button(self, text='登录', command=self.login)
        self.btn_login.grid(row=7, column=1, padx=10, pady=5, sticky=tk.E)


    def login(self):
        login_type = self.type.get()
        username = self.ent_username.get()
        password = self.ent_password.get()
        if login_type == '1':
            # 查询用户表中是否有该用户
            cursor.execute("SELECT * FROM user_login WHERE 用户名='%s' AND 密码='%s'" % (username, password))
            row = cursor.fetchone()
            if row:
                # 跳转到1.py界面
                self.master.destroy()  # 销毁登录窗口
                os.system("python user.py")
                self.master.destroy()
            else:
                tk.messagebox.showerror(title='错误', message='用户名或密码错误')
        elif login_type == '2':
            # 查询管理员表中是否有该管理员
            cursor.execute("SELECT * FROM manage_login WHERE 用户名='%s' AND 密码='%s'" % (username, password))
            row = cursor.fetchone()
            if row:
                self.master.destroy()  # 销毁登录窗口
                # 跳转到2.py界面
                os.system("python manage.py")
                self.master.destroy()
            else:
                tk.messagebox.showerror(title='错误', message='用户名或密码错误')
        else:
            tk.messagebox.showerror(title='错误', message='无效登录类型！')

# 创建主窗口对象
root = tk.Tk()
root.title('用户登录')
root.geometry('400x350')

# 显示登录界面
lf = LoginFrame(master=root)
lf.mainloop()

# 关闭连接
conn.close()
