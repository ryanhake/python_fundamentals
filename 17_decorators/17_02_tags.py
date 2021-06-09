'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''


def para(func):
    def wrapper(*args):
        return func(*args)
    return wrapper

@para
def formatted_text(tags, msg):
    return (f"{tags} {msg} {tags}")


print(formatted_text("<i>", "hello world"))