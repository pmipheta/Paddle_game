from turtle import Turtle , Screen
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.speeds = 0.1
        self.x = 10
        self.y = 10

    def move(self):
        x = self.xcor()+self.x
        y = self.ycor()+self.y
        self.goto(x,y)

    def bounce_y(self):
        self.y*= -1  
    
    def bounce_x(self):
        self.x *= -1
        self.speeds *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.speeds = 0.1
        self.bounce_x()
        