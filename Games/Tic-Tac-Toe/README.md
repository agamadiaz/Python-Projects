# Tic-Tac-Toe game

## Description
This is a two player version of tic-tac-toe. The game is played locally in the users IDE.
The board is printed and the user has to choose where to place their symbol. It is not interactive (meaning the user clicks where they want to go).
The user has to type in which space they would like to place a symbol.

## Game Code Breakdown

Start off by importing random to use later to decide which player goes first.

```
import random  
```

Next, the actual tic-tac-toe board is defined. Here I drew out a board using bars to divide out each 'section' of the board.
The board will use the board variable to place the appropriate symbol (X,O) where the user places them.

```
def playing_board(board): 

    print("|     |     |     |")
    print("|  " + board[1] + "  |  " + board[2] + "  |  " + board[3] + "  |")
    print("|     |     |     |")
    print("|-----------------|")
    print("|     |     |     |")
    print("|  " + board[4] + "  |  " + board[5] + "  |  " + board[6] + "  |")
    print("|     |     |     |")
    print("|-----------------|")
    print("|     |     |     |")
    print("|  " + board[7] + "  |  " + board[8] + "  |  " + board[9] + "  |")
    print("|     |     |     |")
```

Next, it is time to define a function called 'player_choice' to have the user decide which symbol they would like to be.
Once player 1 picks their symbol the other is automatically assigned to player 2

```
def player_choice():  
    letter = ""
    while not (letter == 'X' or letter == 'O'):
        print("Player 1 would you like to be 'X' or 'O'? ")
        letter = input().upper()

    if letter == 'X': 
        return ['X', 'O']
    else:
        return ['O', 'X']
```

Now a function is defined to see who goes first. This is where the random module that was imported at the start is used.
The two options are Player 1 and Player 2.

```
def starting_player():  
    if random.randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"
```

Next, a function is defined to ask the player where they would like to place their symbol.
This converts the players input from a string to an integer so the computer can read where to place the symbol.

```
def move_selection(board):  
    move = " "
    while move not in "1 2 3 4 5 6 7 8 9".split() or not empty_square(board, int(move)):
        print(turn + " select an empty square 1-9: ")
        move = input()
    return int(move)  
```

Now that the player has selected their move; this function, 'place_move' is used to actually place the players choice on the board.
It replaces the empty space with the users symbol. Convert the integer back to a string.

```
def place_move(board, letter, move):  
    board[move] = str(letter)  
    return board
```

Before a move can be placed on the board, the computer needs to check and see if there is an empty space for the symbol to go.
This function 'empty_square' returns a blank space if there is no symbol present. 

```
def empty_square(board, move):  
    return board[move] == " "
```

Once a symbol is placed on the board, the computer needs to check and see if the board is full yet. 
This function, 'full_board', checks the squares 1-9 and see if they are all full.

```
def full_board(board): 
    for i in range(1, 10):
        if empty_square(board, i):
            return False
    return True
```

Now that the computer has checked to see if the move can be placed by checking if there are empty spaces or if the board is full; the computer checks to see if a player has won.

The winning conditions are defined in the function 'winner' with the 8 possible winning conditions defined. All three spaces must have the same symbol to return as a winning condition. Otherwise the game keeps going.

```
def winner(board, win):  
    if board[1] == board[2] == board[3] == win:  # 3 across on top
        return True
    if board[4] == board[5] == board[6] == win:  # 3 across in middle
        return True
    if board[7] == board[8] == board[9] == win:  # 3 across on bottom
        return True
    if board[1] == board[4] == board[7] == win:  # 3 down on left
        return True
    if board[2] == board[5] == board[8] == win:  # 3 down in middle
        return True
    if board[3] == board[6] == board[9] == win:  # 3 down on right
        return True
    if board[1] == board[5] == board[9] == win:  # 3 diagonal top left to bottom right
        return True
    if board[3] == board[5] == board[7] == win:  # 3 diagonal top right to bottom left
        return True
    else:
        return False
```

Once the game is over, the game will ask the players if they want to play again. 
If they do, by entering Y, the game will restart by asking Player 1 what symbol they choose to be.
Anything other than a Y will end and close the game.

```
def play_again():  
    print("Would you like to play again? (Y/N): ")
    if input().upper() == 'Y':
        return True
    else:
        return False
```

Now that everything has been defined it's time to run the game itself

A gameplay loop is set up to have the game cycle through all the functions while the game is active.
- Starting by drawing a blank board
- The players decide which symbol is assigned to each player
- The computer randomly assigns a starting player

```
print("Welcome to Tic Tac Toe")
while True:
    game_board = [" "] * 10  
    player_1, player_2 = player_choice() 
    turn = starting_player()  
    print(turn + " will go first")
    gameplay = True  
```

Now the game will first look at which players turn it is. It will then ask that specific player to select their move on the board.
It will then check if the space is blank and if True then place the players symbol in that space. Then the computer checks if the move fulfills one of the 8 winning conditions. 
- If not, then the next player gets to go.
- If yes, then it appropriately prints out a winning messege or tie game messege.

```
    while gameplay:  
        if turn == "Player 1":  
            playing_board(game_board)  
            move = move_selection(game_board) 
            place_move(game_board, player_1, move)  

            if winner(game_board, player_1):  
                playing_board(game_board)
                print("Player 1 wins!")
                gameplay = False

            else:
                if full_board(game_board):  
                    playing_board(game_board)
                    print("Tie Game")
                    break
                else:
                    turn = "Player 2"

        if turn == "Player 2":  
            playing_board(game_board)
            move = move_selection(game_board)
            place_move(game_board, player_2, move)

            if winner(game_board, player_2):
                playing_board(game_board)
                print("Player 2 wins!")
                gameplay = False
            else:
                if full_board(game_board):
                    playing_board(game_board)
                    print("Tie Game")
                    break
                else:
                    turn = "Player 1"
```

The game is now over with either player 1 or 2 winning or a Tie game. The game then asks the players if they want to play again.

```
    if not play_again():  
        break
```

The game continues until the users no longer wish to play. 
That completes the Tic-Tac-Toe game.

The full code is under the Tic Tac Toe.py file including comments.
