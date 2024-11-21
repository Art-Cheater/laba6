class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


# Пример использования
library = Library()
library.add_book(Book("1984", "George Orwell", 1949))
library.add_book(Book("Brave New World", "Aldous Huxley", 1932))

search_title = "1984"
found_book = library.find_book_by_title(search_title)

if found_book:
    print(f"Book found: {found_book}")
else:
    print(f"Book with title '{search_title}' not found.")