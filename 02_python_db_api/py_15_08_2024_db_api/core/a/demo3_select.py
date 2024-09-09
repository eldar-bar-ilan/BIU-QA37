import mysql.connector as db

# connection to a specified database
con = db.connect(host='localhost', user='root', password='1234', database='db_python')
cursor = con.cursor()

cursor.execute('select * from products')

for i in range(5):
    result = cursor.fetchone()
    print(result)


