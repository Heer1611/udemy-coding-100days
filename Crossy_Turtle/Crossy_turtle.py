import time
from turtle import Screen
from player_crossy import Player
from car_manager import CarManager
from scoreboard_crossy import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

user_turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(user_turtle.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if user_turtle.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if user_turtle.at_finish_line():
        user_turtle.at_starting()
        car_manager.level_up()
        scoreboard.increase_score()

screen.exitonclick()
