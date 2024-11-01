import sqlite3

conn = sqlite3.connect("desafio_final.db")

cursor = conn.cursor()

# cursor.execute("""CREATE TABLE books(
#                book_id int primary key,
#                title varchar(40),
#                author_id int,
#                year_public date,
#                gender vachar(40),
#                foreign key (author_id) references authors(author_id)               
#                ) """)

# cursor.execute("""CREATE TABLE authors(
#                author_id int primary key, 
#                name_author varchar(50))""")

# cursor.execute("""CREATE TABLE loans(
#                loan_id int primary key,
#                book_id int,
#                date_loan date,
#                date_return date,
#                foreign key (book_id) references books(book_id)
#                )""")


# cursor.execute("CREATE TABLE usuarios (id INTEGER, nome TEXT)")

# cursor.execute("")

# cursor.execute("SELECT * from usuarios")
# rows = cursor.fetchall()
# print(rows)
