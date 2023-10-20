from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.hideturtle()
        self.penup()
        self.color('#fff')
        self.goto(x=0, y=210)
        self.write(f'{self.p1_score}:{self.p2_score}', align='center', font=('Courier', 50,'bold'))

    def increase_score(self):
        self.clear()
        print('chegou atee aqui')
        self.goto(x=0, y=210)
        self.write(f'{self.p1_score}:{self.p2_score}', align='center', font=('Courier', 50,'bold'))


    def play_1_score(self):
        self.p1_score += 1
        self.increase_score()
    
    def play_2_score(self):
        self.p2_score += 1
        self.increase_score()

    def game_result(self):
        winner = max((self.p1_score,self.p2_score))
        if winner == self.p1_score:
            winner = 'Player 1'
        else:
            winner = 'Player 2'
        self.goto(0,50)
        self.write(f'Game Over {winner} won!', align='center', font=('Courier', 30,'bold'))
