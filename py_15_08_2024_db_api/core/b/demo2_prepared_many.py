import mysql.connector as db

con = db.connect(host='localhost', user='root', password='1234', database='db_python')
curser = con.cursor(prepared=True)
prepared_stmt = 'insert into products values(0, %s, %s)'

data = [
    ('kandy', 25),
    ('sprite', 11),
    ('coca cola', 11),
    ('after shave', 200),
    ('normalax', 62),
]

curser.executemany(prepared_stmt, data)
con.commit()
con.close()
