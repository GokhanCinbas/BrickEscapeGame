from turtle import *


class Brick(Turtle):
    def __init__(self, color, position):
        super().__init__()
        self.color(color)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.goto(position)
