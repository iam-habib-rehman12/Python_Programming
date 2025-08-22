import mysql.connector as sql

conn=sql.connect(host='127.0.0.1', password='root', user='root', database= "python_db")

if conn.is_connected():
    print("connection established")
else:
    print("connection failed:")

c=conn.cursor()
sql1="""create table student(roll_no varchar(10), name varchar(50), department varchar(50))"""
c.execute(sql1)
c.close()