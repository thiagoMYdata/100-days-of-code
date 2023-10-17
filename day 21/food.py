from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.up()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color('#f66')
        self.speed(0)
        random_x = randint(-240, 240)
        random_y = randint(-240, 240)
        self.goto(x=random_x, y=random_y)
        self.refresh()

    def refresh(self):
        random_x = randint(-240, 240)
        random_y = randint(-240, 240)
        self.goto(x=random_x, y=random_y)
        