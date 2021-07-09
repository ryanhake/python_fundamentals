'''
Write a script that creates a dictionary of keys.txt, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

number = int(10)
myDict = {x:x * x for x in range(1, number + 1)}
print("\nDictionary = ", myDict)