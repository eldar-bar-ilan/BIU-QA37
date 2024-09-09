import mysql.connector as sql

# a connection to the database
con = sql.connect(host='localhost', user='root', password='1234')

# an object for sending SQL queries to the database
cursor = con.cursor()

# creating a new database (if not exist)
sql = 'create database if not exists db_python'
cursor.execute(sql)

cursor.execute("use db_python")

sql = """
create table if not exists products(
id int primary key auto_increment,
product_name varchar(25),
price float
)
"""
cursor.execute(sql)

cursor.execute("insert into products values(0, 'TV', 1700)")
con.commit()
