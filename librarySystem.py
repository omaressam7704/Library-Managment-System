# This module implements the comprehensive Library Management System

class Book:
    def __init__(self, title, author, isbn, price):
        """Initializes a book with title, author, ISBN, and price"""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.issuedTo = None

    def displayDetails(self):
        """Displays book details"""
        status = f"Issued to {self.issuedTo.name}" if self.issuedTo else "Available"
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Price: ${self.price}, Status: {status}")

    def applyDiscount(self, discount):
        """Applies a discount to the book price"""
        self.price -= self.price * (discount / 100)

class Member:
    def __init__(self, name, memberId):
        """Initializes a member with name and member ID"""
        self.name = name
        self.memberId = memberId
        self.issuedBooks = []

    def issueBook(self, book):
        """Issues a book to the member"""
        if book not in self.issuedBooks:
            self.issuedBooks.append(book)

    def returnBook(self, book):
        """Returns a book from the member"""
        if book in self.issuedBooks:
            self.issuedBooks.remove(book)

    def displayIssuedBooks(self):
        """Displays books issued to the member"""
        print(f"{self.name} has issued: {[book.title for book in self.issuedBooks]}")

class Library:
    def __init__(self):
        """Initializes the library with empty lists of books and members"""
        self.books = []
        self.members = []

    def addBook(self, book):
        """Adds a book to the library"""
        self.books.append(book)

    def issueBook(self, book, member):
        """Issues a book to a member"""
        if book in self.books and book.issuedTo is None:
            book.issuedTo = member
            member.issueBook(book)
            self.books.remove(book)
            print(f"Book {book.title} issued to {member.name}")
        else:
            print(f"Book {book.title} is not available")

    def returnBook(self, book, member):
        """Returns a book from a member to the library"""
        if book in member.issuedBooks:
            book.issuedTo = None
            member.returnBook(book)
            self.books.append(book)
            print(f"Book {book.title} returned by {member.name}")

    def viewIssuedBooks(self):
        """Displays all issued books and their holders"""
        for member in self.members:
            print(f"{member.name} has issued: {[book.title for book in member.issuedBooks]}")

class Transaction:
    def __init__(self, book, member, issueDate, returnDate=None):
        """Records a book transaction with issue and return dates"""
        self.book = book
        self.member = member
        self.issueDate = issueDate
        self.returnDate = returnDate

    def returnBook(self, returnDate):
        """Records the return date of a book"""
        self.returnDate = returnDate

# Testing
if __name__ == "__main__":
    library = Library()

    # Adding books to the library
    book1 = Book("1984", "George Orwell", "12345", 15.99)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "67890", 12.99)
    library.addBook(book1)
    library.addBook(book2)
    
    # Adding members to the library
    member1 = Member("John Doe", "001")
    member2 = Member("Jane Smith", "002")
    library.members.append(member1)
    library.members.append(member2)

    # Issuing and returning books
    library.issueBook(book1, member1)
    member1.displayIssuedBooks()
    library.viewIssuedBooks()

    library.issueBook(book2, member2)
    member2.displayIssuedBooks()
    library.viewIssuedBooks()

    library.returnBook(book1, member1)
    member1.displayIssuedBooks()
    library.viewIssuedBooks()
