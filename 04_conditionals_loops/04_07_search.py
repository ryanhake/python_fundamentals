'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

x = int(input("Please print number 0 - 1,000,000,000: "))
y = 0
while x < 1000000000:
    if y <= x:
        print(y)
    y += 1