class Book:
    def __init__(self, title, authors, isbn, year, price, quantity):
        self.title = title
        self.authors = authors  # List of authors
        self.isbn = isbn
        self.year = year
        self.price = price
        self.quantity = quantity
        self.lent_to = None  # Tracks who the book is lent to

    def __str__(self):
        authors_str = ", ".join(self.authors)
        return f"{self.title} by {authors_str} (ISBN: {self.isbn}, Year: {self.year}, Price: ${self.price:.2f}, Quantity: {self.quantity})"
