from turtle import Turtle

class Border(Turtle):
    
    def __init__(self,pos,height,width):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=width , stretch_wid=height)
        self.goto(pos)