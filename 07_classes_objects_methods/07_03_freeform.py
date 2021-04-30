'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''


class Pets:
    def __init__(self, animal, name, color, white_spots, black_spots):
        self.animal = animal
        self.name = name
        self.color = color
        self.white_spots = white_spots
        self.black_spots = black_spots

    def total_spots(self):
        return self.white_spots + self.black_spots

   def __add__(self, other):
        total_spots = self.total_spots() + other.total_spots()
        return total_spots

    def __str__(self):
        return f"{self.name} is a {self.color} {self.animal} with {self.total_spots()} spots."


P = Pets("dog", "Zoey", "white", 3, 2)
F = Pets("cat", "Fang", "black", 1, 1)
all_spots = F + P

print(all_spots)


class Furniture:
    def __init__(self, size, color, type):
        self.size = size
        self.color = color
        self.type = type

    def __str__(self):
        return f"The {self.type} is a {self.size}, {self.color} {self.type}."


F = Furniture("large", "gray", "couch")


class Room:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color

    def __str__(self):
        return f"The {self.name} is very {self.size} and {self.color}."


R = Room("living room", "large", "tan")

print(P)
print(F)
print(R)