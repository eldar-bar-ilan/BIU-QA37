import mysql.connector as db

# connection to a specified database
con = db.connect(host='localhost', user='root', password='1234', database='db_python')
cursor = con.cursor()

cursor.execute('select * from products')

result = cursor.fetchall()
print(result)

for row in result:
    print(row)

