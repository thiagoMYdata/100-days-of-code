from turtle import Turtle
# from time import sleep
class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('circle')
        self.color('#fff')
        self.goto(x=300, y=400)