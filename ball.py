from turtle import *
import random

ball_x = 0
ball_y = -120
speed_x = 3
speed_y = 3


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("gray")
        self.shape("circle")
        self.penup()
        self.goto(ball_x, ball_y)

    def move(self):
        new_y = self.ycor() + speed_y
        new_x = self.xcor() + speed_x
        self.goto(new_x, new_y)

    def bounce_lateral(self):
        global speed_x
        speed_x *= -1

    def bounce_vertical(self):
        global speed_y
        speed_y *= -1




