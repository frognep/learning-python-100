from turtle import Turtle, Screen
from random import randint

my_turtle = Turtle()
my_screen = Screen()
# ---------------------------- #
my_screen.colormode(255)
# ---------------------------- #

my_turtle.shape("turtle")
my_turtle.speed(10)
my_turtle.pensize(10)

def rand_tuple():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)

    return (r, g, b)

def random_color():
    my_turtle.pencolor(randint(0, 255),randint(0, 255),randint(0, 255))

def random_direction(object, distance, angle):
    directions = ["forward", "backward", "left", "right"]

    user_direction = directions[randint(0,3)]

    if user_direction == "forward" or user_direction == "backward":
        if user_direction == "forward":
            object.fd(distance)
        else:
            object.bk(distance)
    else:
        if user_direction == "right" or user_direction == "left":
            if user_direction == "right":
                object.rt(angle)
                object.forward(distance)
            else:
                object.lt(angle)
                object.forward(distance)


for _ in range(200):
    random_direction(my_turtle, 20, 90)
    my_turtle.color(rand_tuple())


# ---------------------------#
my_screen.exitonclick()

# random direction