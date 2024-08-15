# get a connection to db_python
import mysql.connector as db
con = db.connect(host='localhost', user='root', password='1234', database='db_python')

# get a cursor
cursor = con.cursor()

# define sql command
sql = 'update products set price = 200 where id = 4'
sql2 = 'update products set price = price * 0.75 where id = 4'

# execute the sql command using the cursor
cursor.execute(sql2)

# commit the changes using the connection
con.commit()

