from turtle import Turtle, Screen

my_turtle = Turtle()

# draw a square
for line in range(10):
    my_turtle.pd()
    my_turtle.fd(20)
    my_turtle.pu()
    my_turtle.fd(20)



# ---------------------------- #
my_screen = Screen()
my_screen.screensize()
my_screen.exitonclick()