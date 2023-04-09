from turtle import Turtle
from time import sleep
ALIGNMENT = "center"
FONT = ("Ariel", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.UserScore = 0
        self.UpdateScore()
        
    def IncreaseScore(self):
        self.UserScore += 1
        self.clear()
        self.UpdateScore()
        
    def UpdateScore(self):
        self.write(f"Score: {self.UserScore}", align=ALIGNMENT, font=FONT)

    def GameOver(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)