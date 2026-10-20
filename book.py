class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.borrowed = False

    def borrow(self):
        try:
            if self.borrowed:
                raise ValueError("The book is already borrowed")
            self.borrowed = True
        except ValueError:
            print('Value Error Detected')


    def return_book(self):
        if not self.borrowed:
            raise ValueError("The book is not currently borrowed")
        self.borrowed = False


