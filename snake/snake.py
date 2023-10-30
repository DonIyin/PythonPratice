"""
__author = "Iyinoluwa Don-Taiwo
__email = "iyinoluwadontaiwo@gmail.com
__facebookLink__ = "https://www.facebook.com/profile.php?id=61551928469140"
__instagramLink__ = "https://www.instagram.com/don_code_s/"

Snake game desktop GUI application using the following dependencies:
turtle (built-in module)
time (built-in module)
random (built-in module)
date_of_completion =  "21st october 2023"
"""

import turtle
import random
import time

# creating screen
screen = turtle.Screen()
screen.title("DON'S SNAKE GAME")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

# Creating border
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# score
score = 0
delay = 0.1

# snake
snake = turtle.Turtle()
snake.speed()
snake.shape("square") # changed shape to circle
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

# food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("white")
fruit.penup()
fruit.goto(30, 30)

# Storing eaten fruits
old_fruit = []

# scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: ",
              align="center",
              font=("Courier", 24, "bold"))


# define how to move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"


def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"


def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"


def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


# keyboard binding
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# main loop
while True:
    screen.update()

    # snake and food collision
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write(f'Score: {score}',
                      align='center',
                      font=("Courier", 24, "bold"))
        delay -= 0.001
        # defining random snake body colours
        colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

        # Creating new foods
        new_fruits = turtle.Turtle()
        new_fruits.speed(0)
        new_fruits.shape("square")  # changed shape to circle
        new_fruits.color(str(random.choice(colours)))
        new_fruits.penup()
        old_fruit.append(new_fruits)

    # adding ball to snake
    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()

        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)
    snake_move()

    # snake and border collision
    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write(f'Game Over: \nYour score is {score}', align='center', font=("Courier", 30, "bold"))

    # Snake collision
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write(f'Game Over: \nYour score is {score}', align='center', font=("Courier", 30, "bold"))

    time.sleep(delay)

# still having problems in terminating but it can be exempted
turtle.Terminator()

