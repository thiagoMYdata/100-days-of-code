from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


screen_score = ScoreBoard()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.06)
    snake.move()

    if  snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        screen_score.add_point()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        screen_score.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
       
        if snake.head.distance(segment) < 10:
            screen_score.game_over()
            game_is_on = False
            
    




screen.exitonclick()