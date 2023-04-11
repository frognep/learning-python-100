from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shapesize(stretch_wid=5 , stretch_len=1)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(x_pos, y_pos)
 

    def go_up(self):
        current_y = self.ycor()
        self.goto(self.xcor(), current_y + 20)

    
    def go_down(self):
        current_y = self.ycor()
        self.goto(self.xcor(), current_y - 20)