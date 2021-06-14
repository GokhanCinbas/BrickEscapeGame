from turtle import *

dist = 80


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=10, outline=10)
        self.color("lightgray")
        self.goto(0, -300)

    def move_right(self):
        self.forward(dist)

    def move_left(self):
        self.back(dist)
