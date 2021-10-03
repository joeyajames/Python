from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.write("..FINISH LINE..", align="center", font=("Arial", 15, "normal"))


    def loose(self):
        self.goto(0,0)
        self.write("YOU LOOSE..!!", align="center", font=("Arial black", 15, "bold") )

    def win(self):
        self.goto(0,0)
        self.write("YOU WIN..!!", align="center", font=("Arial black", 15, "bold") )
