import time
from os import system
from turtle import Screen
from snake import Snake
from food import Food
from random import randint
from scoreboard import ScoreBoard

def clear():
    system("cls")

clear()
# ------------------------------------#
screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

# ------------------------------------#
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # DETECT COLLISION WITH FOOD

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        scoreboard.increase_score()
        
    # DETECT COLLISION WITH WALL

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()

    # DETECT COLLISION WITH TAIL
    for segment in snake.segment_list[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# ------------------------------------#
screen.exitonclick()