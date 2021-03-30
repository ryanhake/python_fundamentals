'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

#s0 = input("Print 10 numbers please:\n number 1: ")
# s1 = int(input("number 2: "))
# s2 = int(input("number 3: "))
# s3 = int(input("number 4: "))
# s4 = int(input("number 5: "))
# s5 = int(input("number 6: "))
# s6 = int(input("number 7: "))
# s7 = int(input("number 8: "))
# s8 = int(input("number 9: "))
# s9 = int(input("number 10: "))
lst = []
for i in range(1,11):
    number = int(input("give a number: "))
    print("you got the number")
    print(number)
    lst.append(number)
print(lst)

