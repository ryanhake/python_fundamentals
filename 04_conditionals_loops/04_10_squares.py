'''
Write a script that prints out all the squares of numbers from 1- 50

Use a for loop that demonstrates the use of the range function.

'''

number = int(input("Please enter a positive number? "))
if number >= 0:
    for i in range(1, int(number ** 0.5 + 1)):
        perfect_squares = i**2
        print(perfect_squares, end=" ")