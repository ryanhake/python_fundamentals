'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
print(float(3))

print(int(3.0))

print(3.3 // 3)

x = int(input("To multiply, please place an integer for x: "))
y = int(input("To multiply, please place an integer for y: "))
print(x*y)