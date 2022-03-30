# Rock Paper Scissors game

## Description
A rock, paper, scissors game against the computer. The user enters their input and the computer shows what it picked. 

This game is my first game to include a replay function to ask if the user wants to play again.

## Game Code Breakdown

Begin by importing the random module to have the computer randomly select a choice.

```
import random

print("Lets play 'Rock, Paper, Scissors'")
```

Now the game outline is defined by creating a function called 'play'.

This function asks the users input and lists the choices. Then calls random to select from the defined options 'r, p, or s'.
The computer then shows the user what it picked.

```
def play():  
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    print("I picked: " + computer)
```

Inside the same 'play' function the three game conditions are defined; Win, Lose, or Tie game.
The function 'win' is called upon here to check if the user has won against the computer.

The function 'win' is defined after this chunk of code.

```
    if user == computer:
        return "Tie Game"
    if win(user, computer):
        return "You won!"
    return "You lose"
```

Now the 'win' function is defined.
There are three options for the user to win and are defined as follows:

```
def win(player, opponent):
    if (player == 'r' and opponent == 's') or \
            (player == 's' and opponent == 'p') or \
            (player == 'p' and opponent == 'r'):
        return True
```

These are the typical Rock, Paper, Scissors win conditions; Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.

Finally the function to ask the user if they want to play again is defined as 'play_again'.
If the user wants to play again they enter Y and the game loops to the start.

```
def play_again():
    print("Would you like to play again? (Y/N): ")
    if input().upper() == 'Y':
        return True
    else:
        return False
```

Now time to run the game. This calls the game to run while 'True' or as long as the user keeps wanting to play again.
Otherwise if the user enters anything other than Y, then the game ends.

```
while True:
    print(play()) 
    if not play_again():
        break     
```

That is it for this Rock, Paper, Scissors game.

The full code is under the Rock Paper Scissors.py file including comments
