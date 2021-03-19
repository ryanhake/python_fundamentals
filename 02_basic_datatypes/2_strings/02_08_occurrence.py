'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

sentence = input("Please write a sentence: ")
letter = input("PLease write a letter: ")
print(sentence.index(letter))