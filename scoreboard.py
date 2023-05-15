from turtle import Turtle,Screen


class ScorBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.lscor = 0
        self.rscor = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.updateScor()

    def updateScor(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.rscor,align="center",font=('Arial', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.lscor, align="center", font=("Arial", 80, "normal"))

    def lpoint(self):
        self.lscor += 1 
        self.updateScor()

    def rpoint(self):
        self.rscor += 1 
        self.updateScor()
