"""
Write a decorator function that wraps text passed to it in a html <p> tag.
"""


def para(func):
    def wrapper():
        return "<p> " + func() + " <p>"
    return wrapper

@para
def formatted_text():
    return "Hello World"


print(formatted_text())