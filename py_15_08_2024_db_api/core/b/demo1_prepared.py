# prepared statements
"""
a prepared statement is SQL statement with placeholders
the syntax for a placeholder is %s
insert into products values(0, %s, %s)
the actual data are given in a tuple: ('TV', 350)
cursor.execute(sql, ('TV', 350))
"""
import mysql.connector as db
con = db.connect(host='localhost', user='root', password='1234', database='db_python')

curser = con.cursor(prepared=True)
prepared_stmt = 'insert into products values(0, %s, %s)'
data = ('ice cream', 25)
curser.execute(prepared_stmt, data)
con.commit()
con.close()

