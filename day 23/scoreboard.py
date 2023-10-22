from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('#000')
        self.penup()
        self.goto(x=-260, y=250)

        self.level = 1
        self.level_write()

    def level_write(self):
        if self.level <= 5:
            self.clear()
            self.write(arg=f'Level: {self.level}', align='left', font=FONT)

    def game_over(self):
        self.goto(0,0)
        if self.level > 5:
            self.write(arg='YOU WON!', align='center', font=FONT)
        else:
            self.write(arg='GAME OVER!', align='center', font=FONT)

    def level_increment(self):
        self.level += 1
        self.level_write()