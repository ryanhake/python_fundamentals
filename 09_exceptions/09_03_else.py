'''
Write a script that demonstrates a try/except/else.

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
else:
    print('Sorry there was an error.')