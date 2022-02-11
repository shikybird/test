"""
编写一个程序模拟注册和登录的过程
    *创建一个user表包含用户名和密码字段
    *应用程序中模拟注册和登录功能
        注册则输入用户名密码将用户名密码存入到数据库
        (用户名不能重复)

        登录则进行数据库比对，如果有该用户则打印登录成功
        否则让重新输入
"""

import pymysql

# 创建数据库连接
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='apple119',
                     database='stu')
# 创建游标
cur = db.cursor()


# 登录数据库
def do_login():
    while True:
        while True:
            name = input("请输入用户名：").strip()
            # 检验用户名
            sql = f"select * from user where name = '{name}';"
            cur.execute(sql)
            result = cur.fetchone()
            if result is None:
                print("您所输入的用户不存在！")
                continue
            else:
                break

        while True:
            pwd = input("请输入密码：").strip()
            sql = f"select password from user where name = '{name}';"
            cur.execute(sql)
            result = cur.fetchone()[0]
            if pwd == result:
                return
            else:
                print("密码错误！")
                continue


# 注册用户名
def do_register():
    while True:
        name = input("请输入用户名：").strip()
        sql = f"select * from user where name = '{name}';"
        cur.execute(sql)
        result = cur.fetchone()
        if result is None:
            break
        else:
            print("用户名已经存在！")
            continue

    while True:
        pwd1 = input("请输入密码：").strip()
        pwd2 = input("请确认密码：").strip()
        if pwd1 == pwd2:
            print("注册用户成功！")
            break
        else:
            print("两次输入的密码不一致，请重新输入")
            continue
    sql = "INSERT INTO user (name, password) VALUES (%s, %s);"
    try:
        cur.execute(sql, [name, pwd2])
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    return


if __name__ == "__main__":
    while True:
        print("""
            欢迎登录数据库， 请选择：
            1. 登录数据库
            2. 注册数据库
        """)
        choice = int(input("请选择："))

        if choice == 1:
            do_login()
            break
        elif choice == 2:
            do_register()
            break
        else:
            print('再见')
            break
    print("欢迎登录数据库！")
