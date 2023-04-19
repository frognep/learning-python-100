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
        self.last_score = 0
        with open(r"F:\code\udemy\day24\game\data.txt", mode="r") as highscore_file:
            self.high_score = int(highscore_file.read())
        self.update_score()
        
    def increase_score(self):
        self.last_score += 1
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.last_score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.last_score > self.high_score:
            self.high_score = self.last_score
            with open(r"F:\code\udemy\day24\game\data.txt", mode="w") as highscore_file:
                highscore_file.write(f"{self.last_score}")
        self.last_score = 0
        self.update_score()