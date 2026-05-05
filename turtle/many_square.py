import turtle as t
import random
from turtle import Screen
turtle = t.Turtle()
turtle.color("red")
side = [3,4,5,6,7,8,9]
color = ["Red","Orange","Yellow","Green","Blue","Purple","Brown","Dark Gray"]
def shape(num_side):
    angle = 360 / num_side
    for i in range(num_side):
        turtle.right(angle)
        turtle.forward(100)

for shape_side in range(3,11):
    turtle.color(random.choice(color))
    shape(shape_side)

screen = Screen() 
screen.exitonclick()
