# Guessing game

import random  # Calls to import the random function
print("Guess the secret number between 1-10 correctly to win!")
print("You only have 3 tries")

secret_number = random.randint(1, 10)  # Calls the random module to pull a random integer between specified range
guess_count = 0  # Set the guess count at 0
guess_limit = 3  # Set the amount of guesses the use is allowed

# print("FOR TESTING: " + str(secret_number))

while guess_count < guess_limit:  # While count is less than limit the program will keep running
    try:
        guess = int(input("Guess a number: "))
    except ValueError:
        print("Error; please enter a digit 1-10")  # Does not count towards the guess count.
        continue  # If the user inputs anything other than an integer an error will show to the user.
    else:
        guess_count += 1
        if guess >= 11:
            print("The number is between 1-10")
        elif guess != secret_number and guess_count < guess_limit:
            print("Try again")
        elif guess == secret_number:
            print("You guessed correctly!")
            break
else:
    print("Sorry the correct answer was " + str(secret_number))  # Shows correct number changed to a string


# clear labels on the variables help make the code easy to read
# make sure guess is changed to an integer so python can correctly count/add it
# break at the end terminates the loop if guessed correctly otherwise player has 3 chances regardless
