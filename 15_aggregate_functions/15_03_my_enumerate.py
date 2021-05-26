'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''


def my_enumerate(iterable):
    return [v for i, v in enumerate(iterable, start=1) if not i % 2]


seq = list(range(1, 11))

print(my_enumerate(seq))


