# This module defines the Book class

class Book:
    def __init__(self, title, author, price):
        """Initializes a book with a title, author, and price"""
        self.title = title
        self.author = author
        self.price = price

    def displayDetails(self):
        """Displays book details"""
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.price}")

    def applyDiscount(self, discount):
        """Applies a discount to the book price"""
        self.price -= self.price * (discount / 100)

# Testing
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 15.99)
    book1.displayDetails()
    book1.applyDiscount(10)
    book1.displayDetails()
