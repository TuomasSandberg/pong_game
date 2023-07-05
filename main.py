from turtle import Turtle, Screen
from Paddle import Paddle

screen = Screen()
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# move right paddle
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

# move left paddle
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# game_is_on = True
# while game_is_on:


screen.exitonclick()
