'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

s0 = input("Print 10 numbers please:\n number 1: ")
s1 = int(input("number 2: "))
s2 = int(input("number 3: "))
s3 = int(input("number 4: "))
s4 = int(input("number 5: "))
s5 = int(input("number 6: "))
s6 = int(input("number 7: "))
s7 = int(input("number 8: "))
s8 = int(input("number 9: "))
s9 = int(input("number 10: "))
print(s1, s3, s5, s7, s9)
print(s8, s6, s4, s2, s0)