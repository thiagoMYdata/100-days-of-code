from turtle import Turtle, Screen, colormode
from random import randint

def random_color():
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    return r,g,b


turtle = Turtle()
colormode(255)
turtle.speed(0)
turtle.hideturtle()
turtle.width(20)






for y in range(-325, 325 , 71):        
    turtle.up()
    turtle.setx(-325)
    turtle.sety(y)
    turtle.down()

    for _ in range(10):
        turtle.color(random_color())
        turtle.forward(1)
        turtle.up()
        turtle.forward(70)
        turtle.down()    

print(turtle.position())




screen = Screen()
screen.exitonclick()