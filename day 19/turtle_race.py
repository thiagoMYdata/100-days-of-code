from turtle import Turtle, Screen  # , colormode
from random import randint
# colormode(255)

# def random_color():
#     r = randint(1,255)
#     g = randint(1,255)
#     b = randint(1,255)
#     return r,g,b

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title='Make your bet', prompt='Which turtle will win the race? Enter a color (rainbow): ')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

y_options = range(-120, 140+1, 50)

all_turtle = []

# turtle_keys = ['turtle_red', 'turtle_orange', 'turtle_yellow', 'turtle_green', 'turtle_blue', 'turtle_purple']

for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.up()
    new_turtle.goto(x=-230, y=y_options[i])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'congrats {winning_color} turtle won the Turtle bet!')
            else:
                print(f'U lost the {winning_color} turtle won the race!')
            break

        rand_distance = randint(20,40)
        turtle.forward(rand_distance)


screen.exitonclick()
