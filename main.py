import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from lvl_manager import Level
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Road")
screen.tracer(0)

car_manager = CarManager()
player = Player()
level = Level()


screen.listen()
#screen.onkey(hero.up, "Up")
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            level.game_over()
            game_is_on = False

        if player.ycor() > 350:
            level.lvl_up()
            player.reset_position()
            car_manager.speed_up()
screen.exitonclick()