'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
user_inp = str(input("please print a sentence: "))
sentence = user_inp.split()
for word in sentence:
    if sentence.count(word) > 0:
        print(word)