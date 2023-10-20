from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('#000')
screen.title('Pong_game.exe')
screen.tracer(0)



left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))

ball = Ball()
scoreboard = Scoreboard()




screen.listen()



screen.onkeypress(key='w', fun=left_paddle.up)
screen.onkeypress(key='s', fun=left_paddle.down)

screen.onkeypress(key='Up', fun=right_paddle.up)
screen.onkeypress(key='Down', fun=right_paddle.down)
game_state = True

while game_state:
    # x_steps = range(40, 400+1 , 4)
    # y_steps = range(30, 300+1 , 3)
    #  x_list=x_steps[count], y_list=y_steps[count]
    sleep(ball.move_speed)
    ball.move()
    # a.clear()
    
    if ball.ycor() > 270 or ball.ycor() < -260:
        ball.y_bounce()


    
    if ball.xcor() > 380: 
        # print('Left +1 point')
        ball.reset_position()
        scoreboard.play_1_score()
        

    if ball.xcor() < -380:
        # print('Right +1 point')
        ball.reset_position()
        scoreboard.play_2_score()

    # if count < 90 -5:
    #     count += 1

    screen.update()

    if ball.xcor() > 330 or ball.xcor() < -340:
        if ball.distance(left_paddle) <= 50 or ball.distance(right_paddle) <=50:
            ball.x_bounce()
    
    if scoreboard.p2_score == 5 or scoreboard.p1_score == 5:
        scoreboard.game_result()
        ball.goto(0,0)
        screen.update()
        game_state = False

screen.exitonclick()