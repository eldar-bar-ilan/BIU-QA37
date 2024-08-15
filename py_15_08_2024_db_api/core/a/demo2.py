import mysql.connector as db

# connection to a specified database
con = db.connect(host='localhost', user='root', password='1234', database='db_python')
cursor = con.cursor()

list_sql = [
    "insert into products values(0, 'Radio', 230)",
    "insert into products values(0, 'Milk', 8.30)",
    "insert into products values(0, 'Bread', 12)",
    "insert into products values(0, 'Car', 230000)",
    "insert into products values(0, 'Airplane', 25000000)",
]

for sql in list_sql:
    cursor.execute(sql)

con.commit()
