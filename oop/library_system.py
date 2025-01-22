class Book:
    def __init__(self, title, author):
        """Initialize a book with title and author as parameters"""
        self.title = title
        self.author = author
    def __str__(self):
        """We declare the string representation of the book and return a string describing the book"""
        return f"'{self.title}' by {self.author}"
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        """We initialize an Ebook with a title, author, and file size.
        File size of the ebook is an int in MB"""
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """This is a string representation of the book and we shall return a string describing the ebook"""
        return f"{super().__str__()} [Ebook, {self.file_size}MB]"
    
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """We initialize a printBook with page count as an int parameter"""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """We declare a string representation of printbook and return a string describing the book"""
        return f"{super().__str__()} [PrintBook, {self.page_count} pages]"
    
class Library:
    def __init__(self):
        """We initialize a library with an empty collection of books."""
        self.books = []

    def add_book(self, book):
        """We shall add a book, or print instance to the library by using Book, Ebbok, or PrintBook as instances in the parameter"""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise ValueError("Only instances of Book, Ebook, or PrintBook can be added to the library.")
    
    def list_books(self):
        """We list all books in the library"""
        if not self.books:
            print("The library has no books.")
        else:
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book}")
    