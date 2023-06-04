from turtle import Turtle
import random
MOVE_DISTANCE = 5
INCREMENT_MOVE = 10
COLOR = ["purple", "red", "yellow", "green", "blue", "pink"]

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_DISTANCE
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle ("square")
            new_car.color(random.choice(COLOR))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)


    def speed_up(self):
        self.car_speed += INCREMENT_MOVE
