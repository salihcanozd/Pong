from turtle import Turtle

class Paddle(Turtle):
    #raket oluşturuluyor
    def __init__(self,position):
        super().__init__()
        self.yon = 44
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
    #raket yukarı hareket
    def moveUp(self):
        newY = self.ycor() + 15
        #sınıra gelince durması için if kodu
        if self.ycor() >= 240:
            return 0
        self.goto(self.xcor(),newY)
        
    #raket aşağı hareket
    def moveDown(self):
        newY = self.ycor()  - 15
        #sınıra gelince durması için if kodu
        if self.ycor() <= -240:
            return 0
        self.goto(self.xcor(),newY)


    
