from turtle import Turtle , Screen
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.turtle = Turtle("turtle")
        self.turtle.penup()
        self.turtle.color("black")
        self.turtle.left(90)
        self.turtle.goto(0,-280)

    def move_forward(self):
        new_y = self.turtle.ycor() + MOVE_DISTANCE
        self.turtle.goto(self.turtle.xcor(),new_y)

    def reset_positon(self):
        self.turtle.goto(STARTING_POSITION)
        
    def finish_at_line(self):
        if self.turtle.ycor()> FINISH_LINE_Y:
            return True
        else:
            return False

            
