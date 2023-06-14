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

def list_books(event=None):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    if books:
        book_info = "已有书籍如下：\n"
        for book in books:
            book_info += f"书籍编号：{book[0]}，书名：{book[1]}，作者：{book[2]}\n"
        messagebox.showinfo("已有书籍", book_info)
    else:
        messagebox.showerror("错误", "暂无书籍！")

# 创建控件
label1 = tk.Label(root, text="请输入书籍编号：")
entry1 = tk.Entry(root)

label2 = tk.Label(root, text="请输入书籍名称：")
entry2 = tk.Entry(root)

label3 = tk.Label(root, text="请输入书籍作者：")
entry3 = tk.Entry(root)

button1 = tk.Button(root, text="借书", command=lambda: borrow_book(entry1.get()))

button2 = tk.Button(root, text="还书", command=lambda: return_book(entry1.get(), entry2.get(), entry3.get()))

button3 = tk.Button(root, text="查看已有书籍", command=list_books)

# 布局控件
label1.grid(row=0, column=0, padx=5, pady=5)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2.grid(row=1, column=0, padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)

label3.grid(row=2, column=0, padx=5, pady=5)
entry3.grid(row=2, column=1, padx=5, pady=5)

button1.grid(row=0, column=2, padx=5, pady=5)
button2.grid(row=2, column=2, padx=5, pady=5)

button3.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# 定义函数
def borrow_book(book_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE 编号=?", (book_id,))
    book = cursor.fetchone()
    if book:
        cursor.execute("DELETE FROM books WHERE 编号=?", (book_id, ))
        conn.commit()
        messagebox.showinfo("提示", "借书成功！")
    else:
        messagebox.showerror("错误", "没有找到该书籍！")

def return_book(book_id, book_name, book_author):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (编号, 书名, 作者) VALUES (?, ?, ?)", (book_id, book_name, book_author))
    conn.commit()
    messagebox.showinfo("提示", "还书成功！")

# 运行主界面
root.mainloop()