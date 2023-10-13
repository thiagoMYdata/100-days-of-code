from turtle import Turtle, Screen
from time import sleep

# screen configuration
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('My_Snake_Game')
screen.tracer(0)



# start snake body
snake_body = []
x_options = range(0, -120, -20 )
for i in range(3):
    new_turtle = Turtle(shape='square')
    new_turtle.up()
    new_turtle.color('#393')
    new_turtle.goto(x= x_options[i], y=0)
    screen.update()
    snake_body.append(new_turtle)



# print(snake_body) # print a object list

while True:
    for turtle in snake_body:
        new_x =  turtle.position()[0]
        new_y = turtle.position()[1]
        turtle.goto(x= new_x + 20, y = new_y-10)
    sleep(0.1)
    screen.update()



# turtle = Turtle()
# turtle.shape('square')



screen.exitonclick()