class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

     def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"{self.book_id}: {self.title} by {self.author} [{status}]"
        


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print("Book ID already exists!")
        else:
            self.books[book_id] = Book(book_id, title, author)
            print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books in library.")
        else:
            for book in self.books.values():
                print(book)
                

    def issue_book(self, book_id):
        if book_id not in self.books:
            print("Book not found!")
        elif self.books[book_id].is_issued:
            print("Book already issued!")
        else:
            self.books[book_id].is_issued = True
            print("Book issued successfully!")

    def return_book(self, book_id):
        if book_id not in self.books:
            print("Book not found!")
        elif not self.books[book_id].is_issued:
            print("Book was not issued!")
        else:
            self.books[book_id].is_issued = False
            print("Book returned successfully!")


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
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
