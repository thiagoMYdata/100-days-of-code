from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        
        self.high_score = self.load_scoreboard()

        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.score = 0        
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        
        if self.score > self.high_score:
            self.write_scoreboard()
            self.high_score = self.score

        self.clear()
        self.update_scoreboard()


    def load_scoreboard(self):
        path = r'100 days of code\day 24\snake update\score_memory.txt'
        with open(path, mode='r') as file:
            high_score = file.read()

        return int(high_score)


    def write_scoreboard(self):
        path = r'100 days of code\day 24\snake update\score_memory.txt'
        with open(path, mode='w') as file:
            file.write(str(self.score))

