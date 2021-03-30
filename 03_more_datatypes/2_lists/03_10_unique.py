'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
lst = [7, 7, 2, 'hey', 5, 5]
print(lst.count("hey"))
print(lst.count(7))
newlist = []
for item in lst:
    item_is_unique = lst.count(item) < 2
    print("is this item unique?")
    print(item)
    print(item_is_unique)
    if item_is_unique:
        newlist.append(item)
print("here are all the unique items")
print(newlist)
