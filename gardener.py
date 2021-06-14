from turtle import *

class Gardener(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("black")
        self.hideturtle()
        self.pensize(width=1)
        self.penup()
        self.goto(-560, -345)
        self.pendown()
        self.goto(-560, 345)
        self.goto(560, 345)
        self.goto(560, -345)

