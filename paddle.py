from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_axis, y_axis):
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_len=1, stretch_wid=5)  # 20 100 square is 20x20 by default
        self.color("white")
        self.penup()
        self.goto(x=x_axis, y=y_axis)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
