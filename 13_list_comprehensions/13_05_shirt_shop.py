'''
Using a list comprehension, create a *cartesian product* (google this!)
of the given lists.

Then open up your online shop ;)

'''
import itertools

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

for element in itertools.product(['neon orange', 'spring green'], ['S', 'M', 'L']):
    print(element)
