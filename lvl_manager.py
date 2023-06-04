from turtle import Turtle
FONT = ("Courier", 20, "bold")
ALIGNMENT = "center"



class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.goto(-100, 260)
        self.hideturtle()
        self.update_lvl()

    def update_lvl(self):
        self.write(f" Level: {self.level}", align=ALIGNMENT, font=FONT )

    def lvl_up(self):
        self.level +=1
        self.clear()
        self.update_lvl()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)