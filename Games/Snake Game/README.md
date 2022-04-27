# Python Snake Game

## Description
This is a simple version of the classic game of Snake. This version was made using the Turtle module in Python. Turtle allows for the game to be brought up in a seperate screen from the Terminal or the users IDE. The game will instantly restart upon the player hitting a wall or hitting itself. The game will track the players score and set a high score that is only available for each game session.

## Game Code Breakdown

Start by importing the Turtle and Random modules

```
import turtle
import random
```

Next its time to define the size of the game screen, speed of the snake, and the size of the food. The speed (delay) is in milliseconds.

```
WIDTH = 500
HEIGHT = 500
DELAY = 100  
FOOD_SIZE = 10
```

The High Score is defined. To start it is set to 0.

```
high_score = 0
```

Next, the movement parameters are set. This sets what direction and how far the snake moves per each key input by the player.

```
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}
```

Now start to set up the functions that the game will use.
The first four functions define the actual move the user inputs: Up, Down, Left, Right.

```
def move_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"


def move_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"


def move_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"


def move_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"
```

Next the actual game loop is set.

```
def game_loop():
    stamper.clearstamps()  

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]
```

Inside the game loop:

Makes the snake, checks for a collision against itself, checks if food is eaten:

```
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
            or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        reset()
    else:
        snake.append(new_head)  # Adds new head to snake body

        if not food_collision():  # Check food collision
            snake.pop(0)  # Snake stays same length unless it eats one 'food'

        # Snake gets made for the first time.
        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()
```

The rest of the game loop displays the current score, the high score for that game session, and loops (restarts) the game if there is a collision. 

```
        # Sets what the screen will show, both the score and high score will be shown
        screen.title(f"Snake  --  Your Score: {score}   --  High Score: {high_score}")
        screen.update()

        # Loops the game
        turtle.ontimer(game_loop, DELAY)
```


The next function sets the action taken by the game if a 'food' is eaten. This function also checks the current score vs the high score to update it accordingly.

```
def food_collision():
    global food_position, score, high_score
    if get_distance(snake[-1], food_position) < 20:
        score += 1  
        if score > high_score:
            high_score = score  
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False
```

This function sets the random position the 'food' will appear at. The coordinates on the game screen are chosen at random using the random module.

```
def get_random_food_position():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)
```

The length of the snake is set using the following function:

```
def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5  # Pythagoras' Theorem
    return distance
```

Now to set the start of the game and start up the game loop defined earlier. The score is set to 0 for each new game. The snake starts in the middle and moves upward on its own each time the game restarts.

```
def reset():
    global score, snake, snake_direction, food_position
    score = 0
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_direction = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    game_loop()
```

Now using Turtle, it's time to make the actual game play window.

```
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the window dimensions of the game
screen.title("Snake")
screen.bgcolor("gray")  # Sets the color of the background
screen.tracer(0)  # Turns off automatic animation
```

Next, the players input is set to keys for the direction user wants the snake to move. (The up key set to make the snake move up for example).

```
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_right, "Right")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
```

Using the stamper variable, the snakes shape is set and drawn onto the screen.

```
stamper = turtle.Turtle()
stamper.shape("square")  # The shape of the snake and snake body
stamper.penup()
```

Next, the food is defined by shape and color to be drawn on the screen.

```
food = turtle.Turtle()
food.shape("circle")    # Shape of the food
food.color("black")     # Color of the food
food.shapesize(FOOD_SIZE / 20)      # Size of the food
food.penup()
```

After the game loop is completed by either the player colliding with itself or one of the walls; the game is set to replay upon losing.

```
reset()
```

Finally, the game closes only upon the player exiting the game window.

```
turtle.done()
```

This completes the snake game. At this time, this version of the game will not store high scores after the game is closed. 

The full code is under the Snake Game.py file including all comments.

## Turtle Module Documentation

All of the documentation for using the Turtle module can be found at the following:

https://docs.python.org/3/library/turtle.html

All the possible configurations including shapes, colors, stamps, etc. is explained in the documentation of the Turtle Graphics module.
