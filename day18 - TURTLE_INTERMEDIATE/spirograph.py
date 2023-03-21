from turtle import Turtle, Screen
from random import randint

my_turtle = Turtle()
my_screen = Screen()
# --------------------------------#
my_turtle.speed(0)
my_screen.colormode(255)
# --------------------------------#
def random_tuple():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)

    return (r, g, b)

def draw_spirograph(tilt):
    for _ in range(int(360 / tilt)):
        my_turtle.color(random_tuple())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + tilt)

draw_spirograph(5)

my_screen.exitonclick()