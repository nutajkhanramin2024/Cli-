from book import Book
import file_handler

class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self, title, authors, isbn, year, price, quantity):
        new_book = Book(title, authors, isbn, year, price, quantity)
        self.books.append(new_book)
        self.save_books()

    def view_books(self):
        if not self.books:
            print("No books available in the library.")
        for book in self.books:
            print(book)

    def search_books(self, term):
        results = [book for book in self.books if term.lower() in book.title.lower() or term in book.isbn]
        for book in results:
            print(book)

    def search_books_by_author(self, author):
        results = [book for book in self.books if any(author.lower() in a.lower() for a in book.authors)]
        for book in results:
            print(book)

    def remove_book(self, term):
        book_to_remove = None
        for book in self.books:
            if term.lower() in book.title.lower() or term in book.isbn:
                book_to_remove = book
                break
        if book_to_remove:
            self.books.remove(book_to_remove)
            self.save_books()
            print(f"Removed book: {book_to_remove}")
        else:
            print("Book not found to remove.")

    def lend_book(self, term, lent_to):
        for book in self.books:
            if (term.lower() in book.title.lower() or term in book.isbn) and book.quantity > 0:
                book.quantity -= 1
                book.lent_to = lent_to
                self.save_books()
                print(f"Lent book: {book} to {lent_to}")
                return
        print("Not enough books available to lend.")

    def return_book(self, term):
        for book in self.books:
            if (term.lower() in book.title.lower() or term in book.isbn) and book.lent_to:
                book.quantity += 1
                print(f"Returned book: {book}")
                book.lent_to = None
                self.save_books()
                return
        print("Book not found or not lent out.")

    def view_lent_books(self):
        lent_books = [book for book in self.books if book.lent_to]
        for book in lent_books:
            print(f"{book} lent to {book.lent_to}")

    def save_books(self):
        file_handler.save_to_file(self.books)

    def load_books(self):
        self.books = file_handler.load_from_file()
