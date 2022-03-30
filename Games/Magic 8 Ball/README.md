# Magic 8 Ball game

## Description

This is another simple game.
The user asks a question to themselves and presses enter.
The computer then returns the Magic 8 Ball answer.

## Game Code Breakdown

Start off by importing the random module to call for a random integer which will be assigned an answer.

```
import random
```

Next, all of the possible answers are defined.
Each answer is assigned an integer which is how the computer will choose an answer.
There are 9 options here as I later define the choice to be from 1-9. This can be changed to more or less answers.
The answers can be changed as well to return whatever is defined.

```
def getanswer(answer):
    if answer == 1:
        return "Yes"
    elif answer == 2:
        return "Maybe"
    elif answer == 3:
        return "Certainly"
    elif answer == 4:
        return "Without a doubt"
    elif answer == 5:
        return 'Ask again later'
    elif answer == 6:
        return 'Doubtful'
    elif answer == 7:
        return 'No'
    elif answer == 8:
        return 'Slim chance'
    elif answer == 9:
        return 'Not even a sliver of a chance'
```

Now that the answers have been assigned a number, the computer asks the user to think of a question or even type it out.
When the user presses enter the computer then selects a random integer from 1-9. The range can be changed to any range.

```
print("I am the magic 8 ball")
print("Think of a yes or no question and press enter to reveal my answer")
input()

print(getanswer(random.randint(1, 9)))
```
The game then ends. No play again/replay function was created. To play again the program would have to be re-run. Later games I did add replay functions.

The full code is under the Magic 8 ball.py file including comments
