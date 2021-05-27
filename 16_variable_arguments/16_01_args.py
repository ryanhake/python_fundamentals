'''
Write a script with a function that demonstrates the use of *args.

'''

def football_teams(*args):
    for team in args:
        print(f"$ {team}")


football_teams("Giants", "Bucs", "Jets")