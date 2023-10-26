from turtle import Turtle
ALIGNMENT = 'center'
# FONT = ('Courier', 6,'bold')

class WriteState(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)

    def write_to(self, what_should_u_write_and_where:tuple):
        name = what_should_u_write_and_where[0]
        x = what_should_u_write_and_where[1]
        y = what_should_u_write_and_where[2]
        self.goto(x=x,y=y)
        self.write(name, align=ALIGNMENT, font=('Courier', 6,'bold'))
    
    def check_missed_states(self, missed_tuple):
        self.color('#e0414e')
        name_missed = missed_tuple[0]
        x_missed = missed_tuple[1]
        y_missed = missed_tuple[2]
        self.goto(x=x_missed, y=y_missed)
        self.write(name_missed, align=ALIGNMENT, font=('Courier', 8,'bold'))