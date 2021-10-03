from score import Score
from car import Car
from player import Player
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("CROSS_THE_ROAD...")
screen.bgcolor("black")
screen.tracer(0)


player = Player()
car = Car()
car.make_road()
score = Score()

screen.listen()
screen.onkey(player.move, "Up")
playing = True

while playing:
    screen.update()
    time.sleep(0.1)

    car.create_cars()

    car.move()

    for cars in car.all_cars:
        if cars.distance(player) < 23:
            score.loose()
            playing = False

    if player.ycor() >= 270:
        score.win()
        playing = False






screen.exitonclick()