from turtle import Turtle, Screen
from random import randint

my_turtle = Turtle()
my_screen = Screen()
# ---------------------------- #
my_screen.colormode(255)
# ---------------------------- #

# challenge: write function to change pen color between each shape
def random_color():
    my_turtle.pencolor(randint(1, 255),randint(1, 255),randint(1, 255))


shapes_done = False
turtle_sides = 3
while shapes_done != True:
    turtle_angle = 360/turtle_sides
    if turtle_sides <= 10:
        random_color()
        for side in range(turtle_sides):
            my_turtle.fd(100)
            my_turtle.right(turtle_angle)
        turtle_sides += 1
    else:
        shapes_done = False
        my_screen.exitonclick()

# ---------------------------- #






