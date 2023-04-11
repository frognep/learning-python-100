from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# ----------------------------------- #
screen = Screen()
screen.setup(width=800, height=650)
screen.title("Ping Pong")
screen.bgcolor("black")
screen.tracer(0)

# ----------------------------------- #
R_Paddle = Paddle(350,0)
L_Paddle = Paddle(-350,0)
PingPongBall = Ball()
scoreboard = Scoreboard()

# ----------------------------------- #
screen.listen()
screen.onkey(L_Paddle.go_up, "w")
screen.onkey(L_Paddle.go_down, "s")
screen.onkey(R_Paddle.go_up, "k")
screen.onkey(R_Paddle.go_down, "m")

# ----------------------------------- #
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    PingPongBall.move()
    
    # DETECT COLLISION WITH WALL
    if PingPongBall.ycor() > 290 or PingPongBall.ycor() < -290:
        PingPongBall.bounce()

    # DETECT COLLISION WITH PADDLES
    if R_Paddle.distance(PingPongBall) < 50 and PingPongBall.xcor() > 335 or L_Paddle.distance(PingPongBall) < 50 and PingPongBall.xcor() < -335:
        print(PingPongBall.xcor())
        PingPongBall.paddle_hit()


    # DETECT PADDLE BALL MISSES
    if PingPongBall.xcor() > 361:
        scoreboard.l_point()
        PingPongBall.setpos(0, 0)
        PingPongBall.paddle_hit()

    
    if PingPongBall.xcor() < -361:
        scoreboard.r_point()
        PingPongBall.setpos(0, 0)
        PingPongBall.paddle_hit()
    
    

# ----------------------------------- #
screen.exitonclick()