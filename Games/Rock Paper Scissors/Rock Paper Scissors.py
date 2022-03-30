# Rock Paper Scissors game

import random  # Need to import random to generate a random choice by the computer

print("Lets play 'Rock, Paper, Scissors'")


def play():  # We are defining the outline for the game by defining a function as 'play'
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])  # Computer is limited to three selection albeit at random
    print("I picked: " + computer)  # This prints the computers random choice to see what they picked

# Here we set the outputs for the game

    if user == computer:
        return "Tie Game"
    if win(user, computer):
        return "You won!"
    return "You lose"


def win(player, opponent):  # Here we define what the win conditions are
    if (player == 'r' and opponent == 's') or \
            (player == 's' and opponent == 'p') or \
            (player == 'p' and opponent == 'r'):
        return True


def play_again():  # Asks the user if they want to play again
    print("Would you like to play again? (Y/N): ")
    if input().upper() == 'Y':
        return True
    else:
        return False


while True:
    print(play())  # We 'print' the function we created and thus run the program
    if not play_again():  # Once game is over user is asked if they would like to play again
        break
