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
import urllib.parse
import re

url = 'https://pythonprogramming.net/'
values = {'s': 'basics',
          'submit': 'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()
#print(respData)

paragraphs = re.findall(r'<p>(.*?)<p>', str(respData))
for eachP in paragraphs:
    print(eachP)