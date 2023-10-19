from turtle import Turtle
# PADDLE_PLAYER_POSITIONS =  (-350,0) # [(-350, c) for c  in range(40,-40 -1, -20)] 
# PADDLE_COMPUTER_POSITIONS = (350,0) # [(+350, c) for c  in range(40,-40 -1, -20)] 
# UP = 20
# DOWN = -20
# PADDLE_SIZE = len(PADDLE_PLAYER_POSITIONS)


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle( position=position)
        # self.segments_computer = self.create_paddle( position=position)

    def create_paddle(self, position:tuple):
        # paddle = Turtle()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape('square')
        self.color('#fff')
        self.penup()
        self.goto(position)
        # return paddle

    

    # def player_paddle(self):
    #     pass

    # def computer_paddle(self):
    #     pass
    
    def move(self, direction):
        # for num in range(PADDLE_SIZE):
        x = self.xcor()
        new_y = self.ycor() + direction
        self.goto(x = x, y= new_y)


    def up(self):
        self.move(20)

    def down(self):
        self.move(-20)