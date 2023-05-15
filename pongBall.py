from turtle import Turtle

class Ball(Turtle):
    #topu oluşturma
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
    #topun her karede gittigi mesafe
        self.xMove = 10
        self.yMove = 10

    #topun hareketi
    def move(self):
        newX = self.xcor() + self.xMove
        newY = self.ycor() + self.yMove
        self.goto(newX,newY)
    #topun taban veya tavan çarpasındaki yön değiştirme
    def xBounce(self):
        self.yMove = self.yMove * -1
    #topun rakete çarpasındaki yön değiştirme
    def yBounce(self):
        self.xMove = self.xMove*-1

    def ballReset(self):
        self.goto(0,0)
        self.xMove =- self.xMove