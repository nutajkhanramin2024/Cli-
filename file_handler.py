import json
from book import Book

def save_to_file(books, filename="books.json"):
    with open(filename, "w") as file:
        json_books = [book.__dict__ for book in books]
        json.dump(json_books, file, indent=4)

def load_from_file(filename="books.json"):
    try:
        with open(filename, "r") as file:
            json_books = json.load(file)
            books = [Book(**book) for book in json_books]
            return books
    except FileNotFoundError:
        return []
