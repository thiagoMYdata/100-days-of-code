from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24,'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.count_score = 0
        self.up()
        self.color('white')
        self.hideturtle()
        self.goto(x= 0, y= 265)
        self.write(f"Score: {self.count_score}", True, align=ALIGNMENT, font=FONT)

    def clear_board(self):
        self.clear()

    def add_point(self):
        self.count_score += 1
        self.clear()
        self.goto(x= 0, y= 265)
        self.write(f"Score: {self.count_score}", True, align=ALIGNMENT, font=FONT)

        

    def game_over(self):
        self.goto(x=0, y=0)
        self.write('Game OVER', True, align=ALIGNMENT,  font=FONT)