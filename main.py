class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status = "Mavjud" if self.is_available else "Band"
        return f"{self.title} - {self.author} ({status})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                print(f"{title} kitobi olindi.")
                return
        print(f"{title} mavjud emas yoki band.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_available:
                book.is_available = True
                print(f"{title} kitobi qaytarildi.")
                return
        print(f"{title} topilmadi.")

    def show_books(self):
        for book in self.books:
            print(book)


# Test
lib = Library()

b1 = Book("Python Basics", "John Doe")
b2 = Book("OOP in Python", "Jane Smith")

lib.add_book(b1)
lib.add_book(b2)

lib.show_books()
lib.borrow_book("Python Basics")
lib.show_books()
lib.return_book("Python Basics")
lib.show_books()
