# Tic-Tac-Toe game

## Description
This is a two player version of tic-tac-toe. The game is played locally in the users IDE.
The board is printed and the user has to choose where to place their marker. It is not interactive (meaning the user clicks where they want to go).
The user has to type in which space they would like.

## Game Code Breakdown


import random  # Need to call random to generate who goes first


def playing_board(board):  # Drawing the "board"

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


def player_choice():  # Player gets to pick at the start if they want to be 'X' or 'O'
    letter = ""
    while not (letter == 'X' or letter == 'O'):
        print("Player 1 would you like to be 'X' or 'O'? ")
        letter = input().upper()

    if letter == 'X':  # The two possible conditions are defined depending on the players choice
        return ['X', 'O']
    else:
        return ['O', 'X']


def starting_player():  # Calls on random to randomly assign who starts either player 1 or player 2
    if random.randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"


def move_selection(board):  # Asks the user to select a move
    move = " "
    while move not in "1 2 3 4 5 6 7 8 9".split() or not empty_square(board, int(move)):
        print(turn + " select an empty square 1-9: ")
        move = input()
    return int(move)  # Need to convert user input (string) into an integer


def place_move(board, letter, move):  # Assigns where the players choice will go
    board[move] = str(letter)  # Converts the integer into a string for it to be concatenated and printed
    return board


def empty_square(board, move):  # Checks if a square is empty
    return board[move] == " "


def full_board(board):  # Checks if the whole board is full
    for i in range(1, 10):
        if empty_square(board, i):
            return False
    return True


def winner(board, win):  # Sets up all winning conditions
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


def play_again():  # Asks the user if they want to play again
    print("Would you like to play again? (Y/N): ")
    if input().upper() == 'Y':
        return True
    else:
        return False


# Now that everything has been defined it's time to run the game itself


print("Welcome to Tic Tac Toe")
while True:
    game_board = [" "] * 10  # Sets the game board to all blank spaces
    player_1, player_2 = player_choice()  # Calls function player_choice to define which player is 'X' and which is 'O'
    turn = starting_player()  # Calls to see who the starting player will be
    print(turn + " will go first")
    gameplay = True  # Gameplay is now launched

    while gameplay:  # Actual gameplay loop
        if turn == "Player 1":  # On player 1's turn
            playing_board(game_board)  # Shows the current game board
            move = move_selection(game_board)  # Calls for the users input on what their move is
            place_move(game_board, player_1, move)  # Places the users move onto the game board

            if winner(game_board, player_1):  # If player 1's move wins
                playing_board(game_board)
                print("Player 1 wins!")
                gameplay = False

            else:
                if full_board(game_board):  # If tie game
                    playing_board(game_board)
                    print("Tie Game")
                    break
                else:
                    turn = "Player 2"

        if turn == "Player 2":  # On player 2's turn - same conditions as player 1
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

    if not play_again():  # Once game is over user is asked if they would like to play again
        break

#  Game will only end when player declines to play again
