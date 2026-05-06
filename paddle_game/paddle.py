from turtle import Turtle
import time 
class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x,y)
        self.shapesize(stretch_wid=8 ,stretch_len=1)
    
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
    
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)

        