from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("black")
        self.go_to_start()

    def move(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def is_finish_line(self):
        if self.ycor() > 290:
            return True
        else:
            return False
    
    def go_to_start(self):
        self.setpos(STARTING_POSITION)