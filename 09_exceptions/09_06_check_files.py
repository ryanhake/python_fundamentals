'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

with open("integers.txt", "r") as file:
    data = file.read()
    try:
        for i in data[0]:
            print(f"The first integer from 'integers.txt' is {i}.")
            print("1 + 10 = 11")
    except ValueError:
        print('oops. thats not an integer.')
    except IOError:
        print("sorry you can't do that.")


