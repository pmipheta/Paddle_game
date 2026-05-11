from turtle import Turtle

class Scoreboard(Turtle): 
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,200)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def add_score(self):
        self.score += 1
        return self.score
    
    def update_scoreboard(self):
        self.clear() 
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        
        