'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
user_input = int(input("please state a number: "))
mydict = {1: 'january', 2:'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august',
          9: 'september', 10: 'october', 11: 'november', 12: 'december'}
if user_input in mydict:
    print(mydict[user_input])
else:
    print("other")