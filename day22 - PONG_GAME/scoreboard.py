from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Ariel", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.L_score = 0
        self.R_score = 0
        self.updateScoreBoard()


    def l_point(self):
        self.L_score += 1
        self.updateScoreBoard()
    
    def r_point(self):
        self.R_score += 1
        self.updateScoreBoard()
    
    def updateScoreBoard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.L_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.R_score, align=ALIGNMENT, font=FONT)
