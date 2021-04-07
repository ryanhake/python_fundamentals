'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

r = int(input("state number of rows here: "))
x = 1
for i in range(0, r):
    starz = ""
    for j in range(0, x):
       starz += "*"
    x = x + 1
    print(starz)