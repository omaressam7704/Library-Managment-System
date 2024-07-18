# This module contains basic mathematical operations and a factorial function

def add(x, y):
    """Returns the sum of x and y"""
    return x + y

def subtract(x, y):
    """Returns the difference between x and y"""
    return x - y

def multiply(x, y):
    """Returns the product of x and y"""
    return x * y

def divide(x, y):
    """Returns the division of x by y, handling division by zero"""
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def factorial(n):
    """Recursively computes the factorial of n"""
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Testing
if __name__ == "__main__":
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(5, 3))
    print("Multiplication:", multiply(5, 3))
    print("Division:", divide(5, 3))
    print("Factorial:", factorial(5))
