import random

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

print("I am the magic 8 ball")
print("Think of a yes or no question and press enter to reveal my answer")
input()

print(getanswer(random.randint(1, 9)))
