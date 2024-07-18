# Library Management System

This project implements a Library Management System using both functional and object-oriented programming paradigms in Python.

## Project Structure

- `basicFunctions.py`: Contains simple mathematical functions and a recursive factorial function.
- `lambdaFunctions.py`: Contains lambda functions for filtering and mapping data, and sorting a list of tuples.
- `higherOrderFunctions.py`: Contains higher-order functions and a decorator for logging execution time.
- `book.py`: Contains the `Book` class definition.
- `vehicle.py`: Contains the `Vehicle` base class and `Car` and `Bike` subclasses.
- `bankAccount.py`: Contains the `BankAccount` class demonstrating encapsulation.
- `shape.py`: Contains the abstract `Shape` class and its subclasses `Rectangle` and `Circle`.
- `librarySystem.py`: Contains the comprehensive Library Management System implementation, integrating the above parts.

## How to Use

1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/Library-Management-System.git
    cd Library-Management-System
    ```

2. **Run the Individual Parts**
    - For functional programming examples:
        ```bash
        python basicFunctions.py
        python lambdaFunctions.py
        python higherOrderFunctions.py
        ```
    - For object-oriented programming examples:
        ```bash
        python book.py
        python vehicle.py
        python bankAccount.py
        python shape.py
        ```

3. **Run the Comprehensive Library Management System**
    ```bash
    python librarySystem.py
    ```

## Detailed Descriptions

### Functional Programming

#### Basic Functions
- `add(x, y)`: Returns the sum of `x` and `y`.
- `subtract(x, y)`: Returns the difference of `x` and `y`.
- `multiply(x, y)`: Returns the product of `x` and `y`.
- `divide(x, y)`: Returns the division of `x` by `y`, handling division by zero.
- `factorial(n)`: Recursively computes the factorial of `n`.

#### Lambda Functions
- Filters a list of numbers to get only the even ones.
- Maps a list of numbers to their squares.
- Sorts a list of tuples by the second element.

#### Higher-Order Functions
- `applyFunctionToList(func, lst)`: Applies a given function to each element of a list.
- `logExecutionTime(func)`: A decorator that logs the execution time of a function.

### Object-Oriented Programming

#### Book Class
- `__init__(self, title, author, price)`: Initializes a book with a title, author, and price.
- `displayDetails(self)`: Displays book details.
- `applyDiscount(self, discount)`: Applies a discount to the book price.

#### Vehicle, Car, and Bike Classes
- `Vehicle`: Base class with `startEngine` and `stopEngine` methods.
- `Car` and `Bike`: Subclasses that override the `startEngine` method.

#### BankAccount Class
- `__init__(self, initialBalance=0)`: Initializes the account with a balance.
- `deposit(self, amount)`: Deposits an amount to the account.
- `withdraw(self, amount)`: Withdraws an amount from the account.
- `getBalance(self)`: Returns the current balance.

#### Shape, Rectangle, and Circle Classes
- `Shape`: Abstract base class with an abstract `area` method.
- `Rectangle` and `Circle`: Subclasses that implement the `area` method.

### Library Management System

#### Library Class
- Manages lists of books and members.
- Methods for adding books, issuing books, returning books, and viewing issued books.

#### Book Class
- Extended with `isbn` and `issuedTo` attributes.

#### Member Class
- Manages member details and issued books.

#### Transaction Class
- Records book issues and returns with dates and member details.

## Testing

To run the tests, ensure all files are in place and execute the scripts to verify functionality.

## Report

The detailed report on design choices, challenges, and Python concepts applied will be documented separately.
