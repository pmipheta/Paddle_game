from turtle import Turtle , Screen
import time
from Body import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.colormode(255)
screen.title("My snake game")
screen.tracer(0)



snake = Snake()

food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.go_up, "Up")  
screen.onkey(snake.go_down, "Down")   
screen.onkey(snake.go_left, "Left")   
screen.onkey(snake.go_right, "Right")   

gaming = True
while gaming :
    screen.update()
    time.sleep(0.1)
    
    if snake.segment[0].distance(food.turtle) < 15:
        snake.add_segment()
        scoreboard.add_score()

        scoreboard.update_scoreboard()
        food.spawn()
    if snake.segment[0].xcor() > 280 or snake.segment[0].xcor() < -280 or snake.segment[0].ycor() > 280 or snake.segment[0].ycor() < -280 :
        print("Game Over")    
        gaming = False

    for seg in snake.segment[1:]:
        if snake.segment[0].distance(seg) < 10 :
            print("Game Over")
            gaming = False
    snake.move()

screen.exitonclick()