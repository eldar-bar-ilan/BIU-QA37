import mysql.connector as db
con = db.connect(host='localhost', user='root', password='1234', database='db_python')
cursor = con.cursor()
cursor.execute("delete from products where id = 3")
con.commit()
con.close()

