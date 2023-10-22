from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.up_still_press = True
        self.color('#89CFF0')
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up_press(self):
        self.forward(MOVE_DISTANCE)

    def stop(self):
        self.forward(0)
    
    def down_press(self):
        self.backward(MOVE_DISTANCE)

    def level_up(self):
        return self.ycor() > FINISH_LINE_Y
    
    def new_level(self):
        self.goto(STARTING_POSITION)

