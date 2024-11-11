from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PING PONG")
screen.tracer(0)

scorer = ScoreBoard(-100,200)
scorel = ScoreBoard(100,200)
paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle2.move_up, "a")
screen.onkey(paddle2.move_down, "z")

game_on = True
while game_on:
    # Keyboard bindings
    screen.update()
    ball.move()
    time.sleep(0.01)
    #detect collsion with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #detect collision with right paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        print("Made contact")
        ball.bounce_paddle()

    #detect when ball goes out of bounds on right
    if ball.xcor() > 380:
        ball.reset()
        scorer.scorer()

    if ball.xcor() < -380:
        ball.reset()
        scorel.scorel()

    if scorel.lscore == 5 or scorer.rscore == 5:
        game_on = False


win = Turtle()
win.color("teal")
if scorel.lscore == 5:
    win.write(f"Right player wins!, Game Over",align="center",font=("Courier", 30, "normal"))
else:
    win.write(f"Left Player wins!, Game Over",align="center",font=("Courier", 30, "normal"))
# Keep the window open
screen.exitonclick()
