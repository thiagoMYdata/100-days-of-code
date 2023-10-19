from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('#000')
screen.title('Pong_game.exe')
screen.tracer(0)



left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))





screen.listen()

screen.onkeypress(key='w', fun=left_paddle.up)
screen.onkeypress(key='s', fun=left_paddle.down)

screen.onkeypress(key='Up', fun=right_paddle.up)
screen.onkeypress(key='Down', fun=right_paddle.down)

game_state = True

while game_state:
    Ball()
    screen.update()


screen.exitonclick()