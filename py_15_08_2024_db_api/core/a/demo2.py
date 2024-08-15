import mysql.connector as db

# connection to a specified database
con = db.connect(host='localhost', user='root', password='1234', database='db_python')
cursor = con.cursor()
cursor.execute("truncate table products")  # clear table data

list_sql = [
    "(0, 'Radio', 230)",
    "(0, 'Milk', 8.30)",
    "(0, 'Bread', 12)",
    "(0, 'Car', 230000)",
    "(0, 'Airplane', 25000000)",
]

for sql in list_sql:
    cursor.execute(f'insert into products values{sql}')
    print(f'insert into products values{sql}')

con.commit()
con.close()  # closing connection is important to not wast resources
