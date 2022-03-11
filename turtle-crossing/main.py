import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
sleep_time = 0.1
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    # detect player collision with wall
    if player.ycor() > 250:
        sleep_time *= 0.9
        scoreboard.increment_score()
        player.reset_position()

    # detect player collision with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            break

screen.exitonclick()
