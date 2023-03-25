from turtle import Turtle, Screen



screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Which turtle will win the race?", prompt="Enter a color: ")

steve = Turtle(shape="turtle")
steve.penup()
steve.goto(x=-230, y=-100)

screen.exitonclick()