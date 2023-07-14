from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

# move right paddle
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

# move left paddle
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

ball = Ball(380, 285)
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:

    sleep(ball.move_speed)
    ball.move()
    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()


    # Detect when left paddle misses
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()





screen.exitonclick()
