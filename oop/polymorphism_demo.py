import math

#We shall start with the base class shape
class Shape:
    def area(self):
        """We use this method so that it can be overriden by subsequent classes to calculate area"""
        raise NotImplementedError("Derived classes must override this method.")
#We declare derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """We initialize the parameters"""
        self.length = length
        self.width = width

    def area(self):
        """We calculate the area of triengle and return is as float"""
        return self.length * self.width
"""We declare a class of circle"""
class Circle(Shape):
    def __init__(self, radius):
        """We initialize the area of the circle where the params are the radius in float or int"""
        self.radius = radius

    def area(self):
        """We calculate the area of circle to return in float"""
        return math.pi * self.radius **2
        