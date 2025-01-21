class Book:
    def __init__(self, title, author, year):
        """
        We added init constructor to initialize the book attributes.
        Title of the book (str)
        Author of the book (str)
        Publication year (int)
        """
        self.title = title
        self.author - author
        self.year = year
    def __del__(self):
        """ This is a deastructor that prints a message once a book is deleted"""
        print(f"Deleting {self.title}")

    def __str__(self):
        """The string represents the book instance.
        We shall then return a string describing the book in a readable format."""
        return f"'{self.title}' by {self.author}, published in {self.year}"
    def __repr__(self):
        """This is the official string representation of the book instance that can be used to recreate it.
        We shall then return a string that can recreate the book instance."""
        return f"Book('{self.title}', '{self.author}', '{self.year}')"
        