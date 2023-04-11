from random import randint, randrange
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.05)

    screen.update()
    screen.onkey(player.move, "w")

    car_manager.create_car()
    car_manager.move()

    # DETECT COLLISION WITH CARS
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            score_board.game_over()
            game_is_on = False

    # DETECT FINISH LINE
    if player.is_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        score_board.increase_level()
        score_board.updateScoreBoard()
    
screen.exitonclick()