from turtle import Turtle , Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("red")
for i in range(4):
    turtle.right(90)
    turtle.forward(100)


screen = Screen() 
screen.exitonclick()