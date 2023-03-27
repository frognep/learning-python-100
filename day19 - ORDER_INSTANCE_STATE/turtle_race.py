from turtle import Turtle, Screen
from random import randint,choice

race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Which turtle will win the race?", prompt="Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_list = []

# creating turtles at starting line
start_y = -100
for _ in range(6):
    new_turtle = Turtle(shape="turtle")
    turtle_list.append(new_turtle)
    new_turtle.color(colors[_])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_y)
    start_y += 25

if user_bet:
    race_on = True

# turtles move
while race_on:
    random_distance = randint(0, 10)
    random_turtle = choice(turtle_list)
    random_turtle.forward(random_distance)
    if random_turtle.xcor() > 230:
        winning_color = random_turtle.pencolor()
        race_on = False

if winning_color == (user_bet.lower()):
    print("You win!")
else:
    print(f"You lose! {winning_color} won.")

screen.exitonclick()