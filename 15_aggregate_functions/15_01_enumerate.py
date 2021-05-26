'''
Demonstrate the use of the .enumerate() function.
'''

shows = ["Rick and morty", "South park", "Ink Masters"]

for index, show in enumerate(shows, start=1):
    print(f"{index}: {show}")