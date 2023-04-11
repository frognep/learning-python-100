from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-270, 250)
        self.updateScoreBoard()
        
    def updateScoreBoard(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", font=FONT)

    def increase_level(self):
        self.level += 1

    def game_over(self):
        self.clear()
        self.goto(-75, 0)
        self.write(f"GAME OVER", font=FONT)