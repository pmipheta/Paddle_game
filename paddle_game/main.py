from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time 
screen = Screen()

screen.setup(width=800 , height=600)
screen.bgcolor("black")
screen.tracer(0)
paddle1 = Paddle(350,0)
paddle2 = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(paddle1.go_up,"Up")
screen.onkey(paddle1.go_down,"Down")
screen.onkey(paddle2.go_up,"w")
screen.onkey(paddle2.go_down,"s")
gaming = True
while gaming:
    time.sleep(ball.speeds)
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if (ball.distance(paddle1) < 50 and ball.xcor() > 320) or (ball.distance(paddle2) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380 :
        scoreboard.left_point()
        ball.reset_position()
        print("Gameover")
    
    if ball.xcor() < -380:
        scoreboard.right_point()
        ball.reset_position()

    ball.move()
    
screen.exitonclick()