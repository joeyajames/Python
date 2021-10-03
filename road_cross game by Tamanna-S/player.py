from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,-280)
        self.color("white")
        self.shape("turtle")
        self.setheading(90)

    def move(self):
        self.forward(10)