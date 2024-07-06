from tkinter import *

import pymysql


class connne:
    conn1 = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='order')  # 服务器名,账户,密码,数据库名


def conn():
    if connne.conn1: print("连接成功!")


def select(s):
    # 创建游标对象
    cursor = connne.conn1.cursor()

    # 执行SQL查询

    cursor.execute(s.get())

    # 获取查询结果
    result = cursor.fetchall()

    # 遍历结果
    for row in result:
        print(row)

    cursor.close()


def update():
    cursor = connne.conn1.cursor()
    sets="INSERT INTO `foodtable` VALUES ('30','30','30');"
    cursor.execute(sets)
    cursor.close()
    connne.conn1.commit()

    # 删除数据


def delete(s):
    cursor = connne.conn1.cursor()
    cursor.execute(s.get())
    cursor.close()
    connne.conn1.commit()


def view():
    # 创建游标对象
    cursor = connne.conn1.cursor()
    sets = "SELECT * FROM `menus`"
    cursor.execute(sets)
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()


def count():
    # 创建游标对象
    cursor = connne.conn1.cursor()
    sets = "SELECT * FROM `discount_rules`"
    cursor.execute(sets)
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()


def fun_new():
    # 选项按钮
    root = Tk()

    root.geometry("500x400+450+300")
    root.config(bg="white")
    Label(root, text="菜单功能", compound="top").pack()

    # 查询
    label_select = Label(root, text="请输入查询语句")
    label_select.pack()
    entry_select = Entry(root)
    entry_select.pack()
    button1 = Button(root, text="菜单查询", command=view())
    button1.pack()

    label_up = Label(root, text="请输入更新语句")
    entry_up = Entry(root)
    entry_up.pack()
    button3 = Button(root, text="折扣查询", command=count())
    button3.pack()



    # 删除
    label_delete = Label(root, text="请输入要删除的信息")
    entry_delete = Entry(root)
    entry_delete.pack()
    button4 = Button(root, text="点击下单", command=update())
    button4.pack()
    # 视图


    label_view = Label(root, text="请输入视图语句")
    entry_view = Entry(root)
    entry_view.pack()
    button5 = Button(root, text="删除订单", command=lambda: delete(entry_view))
    button5.pack()


    # 存储过程
    label_def = Label(root, text="存储过程")
    entry_def = Entry(root)
    entry_def.pack()
    button6 = Button(root, text="促销活动", command=lambda: delete(entry_def))
    button6.pack()


def denglu():
    if entry_username.get() == "root" and entry_password.get() == "12345":
        print("登陆成功")
        conn()
        fun_new()

    else:
        print("登录错误")


if __name__ == '__main__':
    root = Tk()
    root.geometry("300x300+500+300")

    root.config(bg="white")

    image = PhotoImage(file="C:\\Users\\ironman\\Desktop\\123.png")
    Label(root, image=image, text="校园点菜系统", compound="top").pack()

    label_username = Label(root, text="用户名：")
    label_username.pack()
    entry_username = Entry(root)
    entry_username.pack()

    label_password = Label(root, text="密码：")
    label_password.pack()
    entry_password = Entry(root, show="*")
    entry_password.pack()
    button = Button(root, text="登录系统", command=denglu)
    button.pack()
    mainloop()

