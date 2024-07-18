# This module demonstrates higher-order functions and decorators

import time

def applyFunctionToList(func, lst):
    """Applies a given function to each element of a list"""
    return [func(x) for x in lst]

def logExecutionTime(func):
    """Decorator that logs the execution time of a function"""
    def wrapper(*args, **kwargs):
        startTime = time.time()
        result = func(*args, **kwargs)
        endTime = time.time()
        print(f"Execution time: {endTime - startTime} seconds")
        return result
    return wrapper

# Testing
if __name__ == "__main__":
    def square(x):
        return x ** 2

    print(applyFunctionToList(square, [1, 2, 3, 4, 5]))

    @logExecutionTime
    def slowFunction():
        time.sleep(1)

    slowFunction()
