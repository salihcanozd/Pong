from turtle import Screen,Turtle
from paddle import Paddle
from pongBall import Ball
from scoreboard import ScorBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200,height=720)
screen.title("PONG")

screen.tracer(0)
ball = Ball()
rPaddle = Paddle((350,0))
lPaddle = Paddle((-350,0))

################# Pong Duvar #################
def border(pos,height,width):
    filler = Turtle()
    filler.shape("square")
    filler.color("white")
    filler.penup()
    filler.shapesize(stretch_len=width , stretch_wid=height)
    filler.goto(pos)
    return filler
topBorder = border((0,310),0.6,41.5)
bottomBorder = border((0,-310),0.6,41.5)
leftBorder = border((-410,0),31.5,0.6)
rightBorder = border((410,0),31.5,0.6)
#################             #################           


screen.listen()
screen.onkeypress(rPaddle.moveUp,"Up")  
screen.onkeypress(rPaddle.moveDown,"Down")
screen.onkeypress(lPaddle.moveUp,"w")
screen.onkeypress(lPaddle.moveDown,"s")

scor = ScorBoard()




gameIsOn = True
while gameIsOn:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor()< -280 or ball.ycor() > 280:        
        ball.xBounce()

    if ball.distance(rPaddle) < 50 and ball.xcor()>320 or ball.distance(lPaddle) < 50 and ball.xcor() < -320:
        ball.yBounce()

    if ball.xcor() >= 370:
        ball.ballReset()
        scor.updateScor()
        scor.rpoint()
    if ball.xcor() <= -370:
        ball.ballReset()
        scor.updateScor()
        scor.lpoint()

screen.exitonclick()

