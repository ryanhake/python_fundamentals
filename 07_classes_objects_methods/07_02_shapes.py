'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

import math


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def stats(self):
        return {
            "area": self.length * self.width,
            "perimeter": 2 * (self.length + self.width)
        }

    def __str__(self):
        return f"The area is {self.length * self.width}. The perimeter is {2 * (self.length + self.width)}."


r = Rectangle(10, 5)
print(r)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius **2

    def circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"The area of the circle is {self.area()} and the circumference is {self.circumference()}"

c = Circle(5)
print(c)
