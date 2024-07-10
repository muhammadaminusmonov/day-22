from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

l_score = Scoreboard((-100, 230))
r_score = Scoreboard((100, 230))

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() >= 330) or (ball.distance(l_paddle) < 50 and ball.xcor() <= -330):
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.reset_position()
        l_score.increase_score()

    if ball.xcor() < -390:
        ball.reset_position()
        r_score.increase_score()


screen.exitonclick()
