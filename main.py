from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from car_manager import Carmanager
import time

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = Carmanager()

cars = []

screen.listen()
screen.onkeypress(player.up, "Up")
# screen.onkeypress(player.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False

    #Detect succesfull crossing
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.increase_speed()


screen.exitonclick()
