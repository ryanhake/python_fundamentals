'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

input_str = input("Please enter your name: ")
firstchar = input_str[0]
lastchar = "ay"
print(input_str.replace(input_str,input_str[1:]+firstchar+lastchar))