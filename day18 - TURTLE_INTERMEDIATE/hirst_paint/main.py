from os import system
from random import randint
from colorgram import extract
from turtle import Turtle, Screen

# --------------------------------------#
# creating the turtle and screen object(s)
t_steve = Turtle(visible=False)
t_steve.speed(0)
my_screen = Screen()
my_screen.colormode(255)

# --------------------------------------#
def clear():
    system('cls')

# --------------------------------------#
# function to extract colors from image pallete
def color_extract(image, color_number):
    colors_extracted = extract(image, color_number)

    rgb_list = []
    for color in colors_extracted:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_colors = (r,g,b)
        rgb_list.append(new_colors)

    return rgb_list

rgb_pallete_ex = color_extract('image.jpg', 15)

rgb_pallete_util = [(124, 36, 24), (210, 221, 213), (168, 106, 57), 
                    (222, 224, 227), (186, 158, 53), (6, 57, 83), 
                    (109, 67, 85), (113, 161, 175), (22, 122, 174), 
                    (64, 153, 138), (39, 36, 36), (76, 40, 48)]

# --------------------------------------#
# function to "change" turtle's start position
def setworldcoordinates(object, start_x, start_y):
    # my_turtle.pensize(0)
    object.penup()
    object.setposition(start_x, start_y)
    object.showturtle()

# --------------------------------------#
def dot_line(num_of_dots, start_cor):
    for _ in range(num_of_dots):
        t_steve.penup()
        t_steve.setx(start_cor)
        start_cor += 50
        t_steve.pendown()
        t_steve.pencolor(rgb_pallete_util[randint(0, (len(rgb_pallete_util)-1) )])
        t_steve.dot(30)

# --------------------------------------#
def next_row(object):
    object.penup()
    object_y_cor = object.ycor()
    object_y_cor += 50
    object.sety(object_y_cor)
    
# --------------------------------------#
# MAIN
clear()

setworldcoordinates(t_steve, -300,-200)
steve_x_pos = t_steve.xcor()

count = 10
while count >= 1:
    dot_line(10, steve_x_pos)
    next_row(t_steve)
    count -= 1

t_steve.hideturtle()
# print(len(rgb_pallete_ex))
# --------------------------------------#
my_screen.exitonclick()