from turtle import *
from bricks import Brick
from paddle import Paddle
from ball import Ball
from gardener import Gardener

window = Screen()
window.setup(height=700, width=1200)
window.title("BreakOut Game")
window.bgcolor("black")
window.tracer(0)

colors = ["green", "yellow", "blue", "red", "gray", "white"]

bricks_complete = False
brick_list = []
while not bricks_complete:
    x = -510
    y = 80
    for i in range(6):
        for j in range(13):
            brick_list.append(Brick(color=colors[i], position=(x, y)))
            x += 85
        x = -510
        y += 25
    bricks_complete = True

game_over_announce = Turtle()
game_over_announce.hideturtle()
game_over_announce.penup()
kano = Paddle()
ball = Ball()
sebastian = Gardener()

window.listen()
window.onkey(kano.move_right, "Right")
window.onkey(kano.move_left, "Left")

hit_brick_list = []
game_is_on = True
while game_is_on:
    window.update()
    ball.move()
    # check x limit
    if ball.xcor() <= -555 or ball.xcor() >= 555:
        ball.bounce_lateral()
    # check y limit and paddle touch
    if ball.ycor() >= 345 or abs(ball.xcor() - kano.xcor()) <= 120 and abs(ball.ycor() - kano.ycor()) <= 20:
        ball.bounce_vertical()
    # check hitting to bricks
    for brick in brick_list:
        if abs(brick.ycor()-ball.ycor()) <= 20 and abs(brick.xcor() - ball.xcor()) <= 45:
            ball.bounce_vertical()
            brick.goto(1000, 1000)
            hit_brick_list.append(brick)
    # check missed ball or end game
    if ball.ycor() <= -345:
        game_over_announce.goto(-120, -150)
        game_over_announce.pencolor("white")
        game_over_announce.write("GAME OVER", font=("Arial",30,"normal"))
        game_is_on = False
    if len(hit_brick_list) == len(brick_list):
        game_over_announce.goto(-120, -150)
        game_over_announce.pencolor("white")
        game_over_announce.write("YOU WIN", font=("Arial",30,"normal"))
        game_is_on = False
print(len(brick_list), len(hit_brick_list))



window.mainloop()