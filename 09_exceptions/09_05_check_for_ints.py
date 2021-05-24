'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

try:
    numb = int(input('Please enter a number: '))
    print('My favorite number! ')

except:
    print('Sorry you must enter a number. ')