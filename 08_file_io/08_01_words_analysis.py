'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''


def shortest_words(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    min_len = len(min(words, key=len))
    return [word for word in words if len(word) == min_len]


print("The shortest words in the file are: ", (shortest_words('words.txt')))


def longest_words(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]


print("The longest words in the file are: ", (longest_words('words.txt')))

word_count = 0
with open('words.txt', 'r') as file:
    for line in file:
        word_count += len(line.split())

print("Total number of words: ", word_count)