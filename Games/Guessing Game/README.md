## Description

This is a simple Guess the number game.

The user is guessing the random number the computer has generated.

## Game Code Breakdown

First, import the random module in order for the computer to generate a number to guess.
Then print out what the computer says at the start of the game. 
Tell the user the number is between 1-10 and there are only three tries to guess.

```
import random
print("Guess the secret number between 1-10 correctly to win!")
print("You only have 3 tries")
```

Next a variable is created to use the random module that was imported to call a random integer. 
Here I specified the range 1-10.
After, set the guess count to 0 at the start and set the amount of guesses to 3. 
Either of these can be custom tailored.

```
secret_number = random.randint(1, 10)
guess_count = 0
guess_limit = 3
```

Now the game loop is created using a while statement. 
As long as the guess count is less than 3 the game will ask the user for their guess.
If the user enters something other than a number an error messege will pop up.
If the user enters a number outside of the guessing range, another error messege will pop up.
Neither of the users invalid input will count towards the guess count.

```
while guess_count < guess_limit:  
    try:
        guess = int(input("Guess a number: "))
    except ValueError:
        print("Error; please enter a digit 1-10")  
        continue  
    else:
        guess_count += 1
        if guess >= 11:
            print("The number is between 1-10")
        elif guess != secret_number and guess_count < guess_limit:
            print("Try again")
        elif guess == secret_number:
            print("You guessed correctly!")
            break
```

If the user guesses correctly as seen above, a win statement is printed.
If the user does not guess correctly in the given amount of tries then the computer reveals what the number was.
The integer is then changed to a string in the print statement in order for it to be printed.
```
else:
    print("Sorry the correct answer was " + str(secret_number))
```

The game then ends. No play again/replay function was created. To play again the program would have to be re-run.
Later games I did add replay functions.
