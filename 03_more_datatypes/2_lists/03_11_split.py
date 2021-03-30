'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
user_inp = str(input("please print a sentence: "))
sentence = user_inp.split()
most_common = ""
most_common_count = 0
for item in sentence:
    #determine the count of sentence
    #determine if this count is > most common count, if it is set most common count to this count
    print(item)