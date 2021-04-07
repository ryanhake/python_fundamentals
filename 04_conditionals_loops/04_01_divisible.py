'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''
number = int(input("please state a number 1 - 1,000,000,000: "))
a = 3
if number % a == 0:
    print("Number is divisible by 3")
else:
    print("Number is NOT divisible by 3")
