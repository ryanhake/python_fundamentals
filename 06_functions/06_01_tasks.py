'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results


def if_divisible(number):
    """determine if user input is divisible by 4 or 7"""
    if number % 4 == 0 or number % 7 == 0:
        return "true"
    else:
        return "false"


def both_divisible(number):
    if number % 4 == 0 and number % 7 == 0:
        print("true. number is divisible")
    else:
        print("false. number is not divisible")


user_input = int(input("Please state a number 1 - 1,000,000,000: "))
msg = if_divisible(user_input)
print(msg)
#both_divisible(user_input)