'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''


with open('words.txt', 'r') as file:
    data = file.read().split()
    for x in data[-1:0:-1]:
        print(x[-1::-1], end=" ")
