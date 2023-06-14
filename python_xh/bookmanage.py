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
        book_info = "已有图书如下：\n"
        for book in books:
            book_info += f"编号：{book[0]}，书名：{book[1]}，作者：{book[2]}\n"
        messagebox.showinfo("已有图书", book_info)
    else:
        messagebox.showerror("错误", "暂无图书！")

def add_book(id, name, author):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (编号, 书名,作者) VALUES (?, ?, ?)", (id, name, author))
    conn.commit()
    messagebox.showinfo("提示", "添加图书成功！")

def delete_book(id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE 编号=?", (id,))
    conn.commit()
    messagebox.showinfo("提示", "删除图书成功！")

def update_book(id, name, author):
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET 书名=?, 作者=? WHERE 编号=?", (name, author, id))
    conn.commit()
    messagebox.showinfo("提示", "更新图书信息成功！")

def search_book(id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE 编号=?", (id,))
    book = cursor.fetchone()
    if book:
        messagebox.showinfo("提示", f"编号：{book[0]}，书名：{book[1]}，作者：{book[2]}")
    else:
        messagebox.showerror("错误", "未找到对应图书！")

# 创建控件
label1 = tk.Label(root, text="请输入图书编号：")
entry1 = tk.Entry(root)

label2 = tk.Label(root, text="请输入图书名称：")
entry2 = tk.Entry(root)

label3 = tk.Label(root, text="请输入图书作者：")
entry3 = tk.Entry(root)

button1 = tk.Button(root, text="添加图书", command=lambda: add_book(entry1.get(), entry2.get(), entry3.get()))

button2 = tk.Button(root, text="删除图书", command=lambda: delete_book(entry1.get()))

button3 = tk.Button(root, text="更新图书信息", command=lambda: update_book(entry1.get(), entry2.get(), entry3.get()))

button4 = tk.Button(root, text="查看已有图书", command=list_books)

button5 = tk.Button(root, text="查询图书", command=lambda: search_book(entry1.get()))

# 布局控件
label1.grid(row=0, column=0, padx=5, pady=5)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2.grid(row=1, column=0, padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)

label3.grid(row=2, column=0, padx=5, pady=5)
entry3.grid(row=2, column=1, padx=5, pady=5)

button1.grid(row=3, column=0, padx=5, pady=5)
button2.grid(row=3, column=1, padx=5, pady=5)
button3.grid(row=4, column=0, padx=5, pady=5)
button4.grid(row=4, column=1, padx=5, pady=5)
button5.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# 运行主界面
root.mainloop()