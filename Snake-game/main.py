from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title(titlestring="My Snake Game")
scr.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
scr.listen()
scr.onkey(key="Up", fun=snake.up)
scr.onkey(key="Left", fun=snake.left)
scr.onkey(key="Down", fun=snake.down)
scr.onkey(key="Right", fun=snake.right)

game_is_on = True

while game_is_on:
    scr.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        print("num num num")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_reset()
        snake.reset_snake()

    #Detect collision with snake tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_reset()
            snake.reset_snake()


scr.exitonclick()


