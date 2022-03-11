from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        if random.randint(1, 6) == 3:
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y_cor = random.randint(-250, 250)
            new_car.goto(280, random_y_cor)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(MOVE_INCREMENT)
            if car.xcor() < -310:
                self.cars.remove(car)
