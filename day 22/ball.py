from turtle import Turtle
from time import sleep
from random import randint
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 0.06

        self.x_movement_by = 10
        self.y_movement_by = 10
        
        self.shape('circle')
        self.color('#fff')
        self.penup()
        
        # self.goto(y=self.x_steps, x=self.y_steps )

    def clear(self):
        self.clear()

    def goto_this_place(self, x_list, y_list):
        self.goto(y= y_list, x= x_list )

    def move(self):
        new_x = self.xcor() + self.x_movement_by
        new_y = self.ycor() + self.y_movement_by
        self.goto(x=new_x, y=new_y)
        # sleep(0.1)

    def y_bounce(self):
        self.y_movement_by *= -1
        self.move_speed *=0.95
    
    def x_bounce(self):
        self.x_movement_by *= -1
        self.move_speed *=0.95

    def reset_position(self):
        y_random = randint(-150,150)
        self.move_speed = 0.06

        self.goto(0,y_random)
        self.x_bounce()
        