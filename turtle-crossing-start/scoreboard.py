from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        # self.goto(-100,250)
        self.color("black")
        self.level = 0 
        self.update()
    
    
    def update(self):
        self.clear()
        self.goto(-100,250)
        self.write(f"Level : {self.level}" , align="left", font=FONT)

    def increase_point(self):
        self.level +=1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)