# Import the Turtle Graphics and random modules

import turtle
import random

# Defining the size of the game screen, speed of the snake, and size of the food.

WIDTH = 500
HEIGHT = 500
DELAY = 100  # How fast the snake will move in milliseconds
FOOD_SIZE = 10

# Sets the starting High Score to 0. High score only saved locally per game (i.e. will be 0 each time game is launched)

high_score = 0

# Set the movement parameters per instruction.

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}


# Start to set up the functions that the game will use

# First four functions define the movement the user inputs


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


# Set the actual game loop


def game_loop():
    stamper.clearstamps()  # Removes any existing 'stamps'

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Checks for a collision
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

        # Sets what the screen will show, both the score and high score will be shown
        screen.title(f"Snake  --  Your Score: {score}   --  High Score: {high_score}")
        screen.update()

        # Loops the game
        turtle.ontimer(game_loop, DELAY)


# Sets the action taken by the game if a 'food' is eaten


def food_collision():
    global food_position, score, high_score
    if get_distance(snake[-1], food_position) < 20:
        score += 1  # score = score + 1
        if score > high_score:
            high_score = score  # Sets the high score only if the current score is higher than the old high score
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False


# Sets the random position the 'food' will appear at


def get_random_food_position():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)


# Sets the snakes size


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5  # Pythagoras' Theorem
    return distance


# Sets the start of the game and resets the game if there is a collision


def reset():
    global score, snake, snake_direction, food_position
    score = 0
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_direction = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    game_loop()


# Make the actual game play window
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the window dimensions of the game defined at the start
screen.title("Snake")
screen.bgcolor("gray")  # Sets the color of the background
screen.tracer(0)  # Turns off automatic animation

# Users input for the direction user wants the snake to move (sets which key is assigned which direction)
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_right, "Right")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")

# Sets the drawing of the snake itself
stamper = turtle.Turtle()
stamper.shape("square")  # The shape of the snake and snake body
stamper.penup()

# Sets the drawing of the food
food = turtle.Turtle()
food.shape("circle")    # Shape of the food
food.color("black")     # Color of the food
food.shapesize(FOOD_SIZE / 20)      # Size of the food
food.penup()

# Sets the game for replay upon losing

reset()

# Closes the game upon user exiting the window

turtle.done()
