from turtle import Turtle
import random

COLORS = ["red", "green", "blue", "yellow", "orange", "magenta", "brown"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Carmanager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-240, 220)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

