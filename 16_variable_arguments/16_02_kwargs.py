'''
Write a script with a function that demonstrates the use of **kwargs.

'''


def my_function(**kwarg):
    for item, calories in kwarg.items():
        print(f"{calories} calories in {item}.")


my_function(oreos=300, banana=20, chips=120)