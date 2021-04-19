'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
import random


def roll_dice():
    roll_equals = random.randint(1, 6)
    return roll_equals


def deter_winner(score1, score2):
    print(f"Player 1 rolled {score1}")
    print(f"Player 2 rolled {score2}")
    if score1 > score2:
        print("Player 1 wins!")
    elif score1 == score2:
        print("It's a tie!")
    else:
        print("Player 2 wins!")


player1_score = roll_dice()
player2_score = roll_dice()
deter_winner(player1_score, player2_score)

