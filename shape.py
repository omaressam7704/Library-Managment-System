# This module defines the abstract Shape class and its subclasses Rectangle and Circle

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Abstract method to calculate area"""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        """Initializes a rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculates the area of the rectangle"""
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        """Initializes a circle with a radius"""
        self.radius = radius

    def area(self):
        """Calculates the area of the circle"""
        return 3.14 * (self.radius ** 2)

# Testing
if __name__ == "__main__":
    rect = Rectangle(5, 3)
    circ = Circle(4)

    print("Rectangle Area:", rect.area())
    print("Circle Area:", circ.area())
