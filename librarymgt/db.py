import sqlite3


class Library:
    def __init__(self):
        self.conn = sqlite3.connect("library.db")
        
        self.cursor = self.conn.cursor()
        self.create_table()
        

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            is_issued INTEGER DEFAULT 0
        )
        """)
        self.conn.commit()

    def add_book(self, book_id, title, author):
        try:
            self.cursor.execute(
                "INSERT INTO books (book_id, title, author) VALUES (?, ?, ?)",
                (book_id, title, author)
            )
            self.conn.commit()
            print("Book added successfully!")
        except sqlite3.IntegrityError:
            print("Book ID already exists!")
            

    def view_books(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()

        if not books:
            print("No books in library.")
        else:
            for book in books:
                status = "Issued" if book[3] else "Available"
                print(f"{book[0]}: {book[1]} by {book[2]} [{status}]")
                
                

    def issue_book(self, book_id):
        self.cursor.execute("SELECT is_issued FROM books WHERE book_id = ?", (book_id,))
        result = self.cursor.fetchone()
        

        if not result:
            print("Book not found!")
        elif result[0]:
            print("Book already issued!")
        else:
            self.cursor.execute(
                "UPDATE books SET is_issued = 1 WHERE book_id = ?",
                (book_id,)
            )
            self.conn.commit()
            print("Book issued successfully!")

    def return_book(self, book_id):
        self.cursor.execute("SELECT is_issued FROM books WHERE book_id = ?", (book_id,))
        result = self.cursor.fetchone()

        if not result:
            print("Book not found!")
        elif not result[0]:
            print("Book was not issued!")
        else:
            self.cursor.execute(
                "UPDATE books SET is_issued = 0 WHERE book_id = ?",
                (book_id,)
            )
            self.conn.commit()
            print("Book returned successfully!")
            

    def close(self):
        self.conn.close()


def main():
    library = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            library.add_book(book_id, title, author)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            book_id = input("Enter Book ID to issue: ")
            library.issue_book(book_id)

        elif choice == "4":
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == "5":
            library.close()
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")



if __name__ == "__main__":
    main()
