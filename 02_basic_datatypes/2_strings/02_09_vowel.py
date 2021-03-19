'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

def isvowel(c):
    return (c == "a") or (c == "e") or (c == "i") or (c == "o") or (c == "u")
input_string = input("Enter sentence: ")
vowel_count = 0
for ch in input_string:
    if isvowel(ch):
        vowel_count +=1
print("Total vowel count : {}".format(vowel_count))