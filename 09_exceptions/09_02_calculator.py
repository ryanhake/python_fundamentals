'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''
try:
    dividend = int(input('Please enter a number: '))
    divisor = int(input('And another number: '))
    result = dividend / divisor
    print(f'{dividend} divided by {divisor} equals {result}')
except ZeroDivisionError:
    print('Sorry but you cannot divide by zero.')
except ValueError:
    print('Sorry but you must use a number.')