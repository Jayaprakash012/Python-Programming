from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Child class
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Object creation
r = Rectangle(5, 3)
print("Area of Rectangle:", r.area())