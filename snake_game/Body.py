from turtle import Turtle , Screen

start_position = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.segment = []
        self.create()
        
    def create(self):
        for position in start_position:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            new_segment.penup()
            self.segment.append(new_segment)

    def add_segment(self):
        news = Turtle("square")
        news.penup()
        news.color("white")
        new_piece = self.segment[-1].position()
        news.goto(new_piece)
        self.segment.append(news)

    def move(self):
        for seg in range(len(self.segment)-1,0,-1):
            new_x = self.segment[seg-1].xcor()
            new_y = self.segment[seg-1].ycor()
            self.segment[seg].goto(new_x,new_y)
        self.segment[0].forward(20)

    def go_up(self):
        if self.segment[0].heading() != 270 :
            self.segment[0].setheading(90)
    def go_down(self):
        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)
    def go_left(self):
        if self.segment[0].heading() != 0:
            self.segment[0].setheading(180)
    def go_right(self):
        if self.segment[0].heading() != 180:
            self.segment[0].setheading(0)
     