# This module demonstrates the use of lambda functions for filtering, mapping, and sorting

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumbers = list(filter(lambda x: x % 2 == 0, numbers))
squaredNumbers = list(map(lambda x: x ** 2, numbers))
tuples = [(1, 3), (4, 2), (5, 1), (2, 4)]
sortedTuples = sorted(tuples, key=lambda x: x[1])

# Testing
if __name__ == "__main__":
    print("Even Numbers:", evenNumbers)
    print("Squared Numbers:", squaredNumbers)
    print("Sorted Tuples:", sortedTuples)
