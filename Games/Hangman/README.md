# Hangman Game

## Description

This is a hangman version 1. This version does not print the hangman graphic only shows the amount of lives left, the letters the user has already guessed, the word to guess with '-' for each hidden letter, and the users input.

## Game Code Breakdown

To start, the random and string modules need to be imported.

The possible words chosen by the computer are under a file named 'word_list'. 
This file contains a variable called 'words' that has stored all the possible words. This list can be appended to add or remove words.

``` 
import random
import string

from word_list import words
```
Next I start to define functions for the game.

First function is named 'get_word'. 
This calls for the computer to select a random word from the word choices inside the 'words' variable in the 'word_list' file.
The word is then converted to all uppercase to make it easier for the user to view.

```
def get_word():
    word = random.choice(words)
    return word.upper()
```
The second function is the 'hangman' function. 
This function defines the actual gameplay.

Inside this function first a word is chosen by the computer. Then certain variables are defined. They cover: Amout of letters in the word, makes users letters all capitals, sets the amount of letter guessed by the user, and the amount of lives the user is given.

```
def hangman():
    word = get_word()
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase) 
    used_letters = set()  
    lives = 8
```

Now the game conditions are set. 
The amount of lives left and the letters already used are shown to the user during each guess.
The used letters are sorted in alphabetical order for a better user experience.

```
    while len(word_letters) > 0 and lives > 0:  
        print("Lives left: ", lives)  
        print("Letters used: ", " ".join(sorted(used_letters)))
```        

Now each letter in the word is set to a '-' if not yet guessed.

```
        word_list = [letter if letter in used_letters else '-' for letter in word]  
        print("Guess the word: ", " ".join(word_list))
```

Next, the user is asked to guess a letter.
Once the user guesses a letter, conditions are defined as to what happens next.

If the user guessed a letter that is NOT in the word, the letter is added to the used letters list.
If the user guesses a letter IN the word, the letter is revealed in the correct spot in the word.
User then loses a life if the word is not fully guessed.

```
        user_letter = input("Guess a letter: ").upper()  
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)  
            print(" ")
            if user_letter in word_letters:
                word_letters.remove(user_letter)  
            else:
                lives -= 1  
```

If the user guesses a letter they have already guessed or enters a non letter, then error messeges are displayed to the user.

```
        elif user_letter in used_letters:
            print(" ")
            print("You have already guessed that letter. Try again.")  
            print(" ")
        else:
            print(" ")
            print("Error: Not a valid character")  
            print(" ")
```

If the user has run out of lives without correctly guessing the word, then a losing messege is displayed.

The computer then displays what the word was.

```
    if lives == 0:
        print("Sorry, you have been hung")
        print("The word was: " + word)  
```

If the user correctly guesses all the letters and thus the word without running out of lives, then a winning messege is displayed.

```
    else:
        print("Congratulations! You guessed the word " + word)
```

Finally the function to ask the user if they want to play again is defined.
If the user chooses Y then the game restarts with a new letter to guess.
Anything other than Y ends the game.

```
def play_again():  # Asks the user if they want to play again
    print("Would you like to play again? (Y/N): ")
    if input().upper() == 'Y':
        return True
    else:
        return False
```

Now executes the game when it is ran.
When the game is over user is asked if they want to play again.

```
while True:
    hangman()  
    if not play_again():  
        break
```

That is all for this hangman game. Again it does not display a traditional hangman graphic with body parts added per incorrectly guessed letter.

The full code is under the Hangman Game.py file including comments.

The list of words is under the word_list.py file. Any word can be added or removed from the list.
