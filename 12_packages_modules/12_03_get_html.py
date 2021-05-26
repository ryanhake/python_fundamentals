'''
In 3 lines of code, fetch the HTML text from codingnomads' main page
and print it to your console.

TIP:
- if you wonder what to use, google something like
    "most popular python package"
- if you run into encoding/decoding errors, you're experiencing something
    very common. head over to SO and find a solution!

'''
import urllib.request
from bs4 import BeautifulSoup
page = urllib.request.urlopen("https://codingnomads.co/").read()
html = BeautifulSoup(page, "html.parser")

print(html.get_text())