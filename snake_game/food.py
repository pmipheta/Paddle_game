from turtle import Turtle , Screen
import random
class Food:
    def __init__(self):
        self.turtle = Turtle("circle")
        self.turtle.color("red")
        self.turtle.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.turtle.speed("fastest")
        self.turtle.penup()
        self.spawn()
    
    def spawn(self):
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        self.turtle.goto(x,y)
