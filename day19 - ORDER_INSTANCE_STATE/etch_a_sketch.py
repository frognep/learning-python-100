from turtle import Turtle, Screen

t_steve = Turtle()
my_screen = Screen()



def clear_screen():
    my_screen.resetscreen()

def move_forward():
    t_steve.fd(10)

def move_backwards():
    t_steve.bk(10)

def turn_left():
    current_heading = t_steve.heading()
    t_steve.setheading(current_heading + 10)

def turn_right():
    current_heading = t_steve.heading()
    t_steve.setheading(current_heading - 10)

my_screen.listen()

my_screen.onkey(fun=move_forward, key="w")
my_screen.onkey(fun=move_backwards, key="s")
my_screen.onkey(fun=turn_left, key="a")
my_screen.onkey(fun=turn_right, key="d")
my_screen.onkey(fun=clear_screen, key="c")

my_screen.exitonclick() 