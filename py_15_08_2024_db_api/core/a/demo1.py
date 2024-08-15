import mysql.connector as sql

# a connection to the database
con = sql.connect(host='localhost', user='root', password='1234')

# an object for sending SQL queries to the database
cursor = con.cursor()

# creating a new database (if not exist)
sql = 'create database if not exists db_python'
cursor.execute(sql)


