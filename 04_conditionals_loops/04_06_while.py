'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''

num = 1
while num < 1001:
    if not num % 5:
        print(num)
    num += 1