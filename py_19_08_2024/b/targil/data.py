import mysql.connector as db


class Book:
    def __init__(self, isbn: int = 0, title: str = '', author: str = ''):
        self.isbn = isbn
        self.title = title
        self.author = author


# add function that gets a book as parameter and adds it to the books table in the db
def add_book(book: Book):
    with db.connect(host='localhost', user='root', password='1234', database='db_library') as con:
        # connect to the db_library db
        # get a cursor
        cursor_ = con.cursor(prepared=True)
        # define an sql command
        sql = f'insert into books values(0, %s, %s)'
        # execute the command
        cursor_.execute(sql, (book.title, book.author))
        # use the connection to commit
        con.commit()
        # close the connection (unless you used with)


with db.connect(host='localhost', user='root', password='1234') as con:
    cursor = con.cursor()
    # create a database named db_library
    cursor.execute('create database if not exists db_library')
    cursor.execute('use db_library')
    # create a table named books with isbn, title, author
    cursor.execute('''
    create table if not exists books(
    isbn int primary key auto_increment,
    title varchar(50),
    author varchar(30)
    )''')
