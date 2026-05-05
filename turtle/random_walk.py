from turtle import Turtle, Screen
import random


screen = Screen()
screen.colormode(255) 


turtle = Turtle()
turtle.pensize(20)
turtle.speed(10)

direction = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def random_walk():
    for i in range(500):
        turtle.color(random_color())
        turtle.forward(30)
        turtle.right(random.choice(direction))

random_walk()

screen.exitonclick()