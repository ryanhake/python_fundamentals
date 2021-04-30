'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car:
    """A class that represents a car with a model, a year
       and a speed, plus accelerate and brake methods to
       alter the speed, plus a honk_horn method.
    """
    def __init__(self, model, year, speed=0):
        """Initialiser"""
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        """Speed goes up by 5."""
        self.speed += 5

    def brake(self):
        """Speed goes down by 5"""
        self.speed = max(0, self.speed - 5)

    def honk_horn(self):
        """Print a beep-beep message"""
        print("{} goes 'beep beep'".format(self.model))

my_car = Car("Toyota", "1999", "20")
print(my_car.speed)
print(my_car.honk_horn())