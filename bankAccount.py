# This module defines the BankAccount class with encapsulation

class BankAccount:
    def __init__(self, initialBalance=0):
        """Initializes the account with a balance"""
        self.__balance = initialBalance

    def deposit(self, amount):
        """Deposits an amount to the account"""
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        """Withdraws an amount from the account"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def getBalance(self):
        """Returns the current balance"""
        return self.__balance

# Testing
if __name__ == "__main__":
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(30)
    print("Current Balance:", account.getBalance())
