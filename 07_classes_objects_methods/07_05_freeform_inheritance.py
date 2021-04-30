'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''


class Vehicle:
    """
    This vehicle class was made to show different types of transportation.
    """
    def __init__(self, year, brand, horsepower=0):
        self.year = year
        self.brand = brand
        self.horsepower = horsepower

    def __str__(self):
        return f"The Vehicle is a {self.year} {self.brand}, with {self.horsepower} horsepower."


c = Vehicle(2021, 'Tesla', 500)


class Truck(Vehicle):
    def __init__(self, year, brand, horsepower, gas):
        super().__init__(year, brand, horsepower)
        self.gas = gas

    def __str__(self):
        return f"The Vehicle is a {self.year} {self.brand}, with {self.horsepower} horsepower and {self.gas} fuel."


t = Truck(2020, 'Ram', 305, 'diesel')


class Motorcycle(Truck):
    def __init__(self, year, brand, horsepower, exhaust, gas):
        super().__init__(year, brand, horsepower, gas)
        self.exhaust = exhaust

    def __str__(self):
        return f"""
The Vehicle is a {self.year} {self.brand}, with {self.horsepower} horsepower, {self.exhaust} and {self.gas} fuel."""


m = Motorcycle(2011, 'Yamaha', 200, 'dual exhaust', 'high octane')


print(c)
print(t)
print(m)