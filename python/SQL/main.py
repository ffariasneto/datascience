from desafiosql import *

# book_id = int(input("Digite o ID do Livro: "))
# title = input("Digite o Título do Livro: ")
# author_id = int(input("Digite o ID do Autor: "))
# year_public = input("Digite o ano de publicação: ")
# gender = input("Digite o gênero do livro: ")

# cursor.execute("""INSERT INTO books(book_id, title, author_id, year_public, gender) 
#                VALUES (?, ?, ?, ?, ?)""", (book_id, title, author_id, year_public, gender))

# conn.commit()
# conn.close()

cursor.execute("SELECT * from books")
rows = cursor.fetchall()
print(rows)