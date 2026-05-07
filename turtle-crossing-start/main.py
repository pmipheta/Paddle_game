import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(player.move_forward,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()


    car.move_cars()

    for single_car in car.all_car:
        if single_car.distance(player.turtle)< 20:
            game_is_on = False
            score.game_over()
            
    if player.finish_at_line() :
        score.increase_point()
        car.increase_speed()
        player.reset_positon()
screen.exitonclick()