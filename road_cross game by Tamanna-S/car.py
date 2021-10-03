from turtle import Turtle
import random

COLORS = ["red", "blue", "chartreuse", "aqua", "yellow", "purple",  "deeppink", "fuchsia"]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []

    def create_cars(self):
        random_choice= random.randint(1,6)
        if random_choice == 1:

            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_len=4, stretch_wid=1.5)
            y_pos = random.randint(-240, 250)
            car.goto(300, y_pos)
            car.color(random.choice(COLORS))
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(20)

    def make_road(self):
        road = Turtle()
        road.hideturtle()
        road.color("white")
        road.penup()
        road.goto(-280, -250)
        road.setheading(0)
        while road.xcor() < 280:
            road.pendown()
            road.forward(20)
            road.penup()
            road.forward(10)
        road.penup()
        road.goto(-280, 270)
        while road.xcor() < 280:
            road.pendown()
            road.forward(20)
            road.penup()
            road.forward(10)

            

