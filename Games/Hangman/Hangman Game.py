# Hangman Game

import random  # Calls random to randomize words
import string

from word_list import words  # reference to the .py file 'word_list' that contains the list of words.


# The file is 'word_list' and inside the file 'words' is the variable that has stored all the words


def get_word():  # Making a function to grab the random word for the game
    word = random.choice(words)
    return word.upper()  # Making the word all uppercase to help keep everything the same syntax


def hangman():
    word = get_word()
    word_letters = set(word)  # Amount of letters in the word
    alphabet = set(string.ascii_uppercase)  # Sets the alphabet to all uppercase
    used_letters = set()  # The letter's the user has already guessed that are incorrect
    lives = 8  # Sets the amount of lives the user gets

    #  print(word) FOR TESTING PURPOSES

    while len(word_letters) > 0 and lives > 0:  # Sets the conditions for the game to run
        print("Lives left: ", lives)  # Shows user the amount of lives they have left
        print("Letters used: ", " ".join(sorted(used_letters)))
        # Shows user the letter they have already guessed and sorts the guessed letters alphabetically

        word_list = [letter if letter in used_letters else '-' for letter in word]  # Sets word to '---' until guessed
        print("Guess the word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()  # Asks the user to guess a letter
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)  # Adds the users guess to the 'used letters' of the game
            print(" ")
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # Removes the letter user guessed from the word letters
            else:
                lives -= 1  # If user guesses incorrectly they lose a life

        elif user_letter in used_letters:
            print(" ")
            print("You have already guessed that letter. Try again.")  # If user guesses a letter they already guessed
            print(" ")
        else:
            print(" ")
            print("Error: Not a valid character")  # If user enters a non-letter
            print(" ")

    if lives == 0:
        print("Sorry, you have been hung")
        print("The word was: " + word)  # Shows what the word was if user loses

    else:
        print("Congratulations! You guessed the word " + word)


hangman()  # Runs the game
