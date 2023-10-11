from turtle import Turtle, Screen, colormode

turtle = Turtle()
colormode(255)

turtle.shape('arrow')
turtle.color('#626ebb')
turtle.speed(0)
# turtle.hideturtle()

## First challenge

# for j in range(100, 150):
#     for i in range(2):        
#         turtle.forward(j+i)
#         turtle.right(90)
#         turtle.forward(j)
#         turtle.right(90)

# turtle.width(2)


## Second challenge

# for c in range(14):
#     turtle.forward(7)
#     turtle.up()
#     turtle.forward(4)
#     turtle.down()
# turtle.forward(7)


## Third challenge
##360/L if result is int()

# list_integer_number = [q for q in range(3,11)]

# for index, value in enumerate( list_integer_number):
#     for _ in range(list_integer_number[index]):
#         turtle.forward(125)
#         k = list_integer_number[index]
#         turtle.right(360/k)


## fourth challenge
# from random import choice
# def random_walking():
#     colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#     # angle = [0, 90 , 180, 270,]
#     angle = range(0, 360, 60)
#     random_color = choice(colours)
#     random_path = choice(angle)
#     return random_color, random_path

# for i  in range(150):
#     turtle.hideturtle()
#     action =  random_walking()
#     turtle.width(10)
#     turtle.color(action[0])
#     turtle.setheading(action[1])
#     turtle.forward(50)

## fifth challenge
from random import randint

def random_color():
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    return r,g,b

# turtle.color(random_color())

turtle.hideturtle()

for i in range(0,361,1):
    # turtle.color(random_color())
    turtle.circle(80)
    turtle.setheading(i)



screen = Screen()
screen.exitonclick()




