import sqlite3
db = sqlite3.connect("ebookstore_db")
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, 
               author TEXT, qty INTEGER)
''')
db.commit()

cursor = db.cursor()

data = [
    (3001, 'A Tale of Two cities', 'Charles Dickens', 30),
    (3002, 'Harry Potter and the Philosopher\s Stone', 'J.K. Rowling', 40),
    (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis ', 25),
    (3004, 'The Lord of the Rings', 'J.R.R Tolkien ', 37),
    (3005, 'Alice in Wonderland', 'Lewis Carroll ', 12) 
]
stmt = "INSERT OR IGNORE INTO book (id,title,author,qty) VALUES (?, ?, ?, ?)"
cursor.executemany(stmt,data)

db.commit()


def enter_book(add_id, add_title, add_author, add_qty):
    """This function inserts a new book into the table
    """
    cursor.execute('''INSERT INTO book(id,title,author,qty)
               VALUES(?,?)''',(add_id, add_title, add_author, add_qty))
   
    db.commit()


def update_book(id, updated_title, updated_author, updated_qty):
    """This function updates the information on the book of the id selected by user
    """
    cursor.execute('''UPDATE book SET title = ?, author = ?, qty = ? WHERE id = ?''',(id, updated_title, updated_author, updated_qty))
   
    db.commit()


def delete_book(id_for_delete):
    """This function deletes the book with id selected by the user
    """
    cursor.execute('''DELETE FROM book where id = ?''',(id_for_delete,))
   
    db.commit()


def search_books(title):
    """This functions allows the user to search for a book by title provided by the user
    """
    cursor.execute('''SELECT id,title,author,qty FROM book  WHERE title=?''',(title))
    
    db.commit()


while True:
    print("1.Enter book\n2. Update book\n3. Delete book\n4. Search books\n0. Exit")
    
    option = input("Select your option:  ")

    try:
        if option == "1":
            add_id = input('Enter the id of the book')
            add_title = input('Enter the title of the book')
            add_author = input('Enter the author of the book')
            add_qty = input('Enter the qty of the book')
            enter_book(add_id, add_title, add_author, add_qty)
    
        elif option == "2":
            id = input('Enter the id of the book you want to update')
            updated_title = input('Enter the updated title')
            updated_author = input('Enter the updated author')
            updated_qty = input('Enter the updated title')
            update_book(id, updated_title, updated_author, updated_qty)
        elif option == "3":
            id_for_delete = input('Enter id of the book you would like to delete')
            delete_book(id_for_delete)
        elif option == "4":
            search = input('What is the title of the book you would like to search?')
            search_books(search)
        elif option == "0":
            print('Exiting')
        else:
            print('Invalid option, please try again')
    finally:
        print('Closing')
        break
db.close()
