from turtle import Turtle, Screen
from time import sleep


def head_movement(snake_body:list, direction:str):
    head =  snake_body[0]
    position = head.position()
    if direction == 'w':
        head.left(90)
        head.forward(20)
        return position
    elif direction == 'd':
        head.forward(20)
        return position

def connect_movement(snake_body:list , direction):
    # snake_body.reverse()
    segment_position_memory = head_movement(snake_body,  direction)
    # for _ in len(snake_body) - 1:
    
    for turtle in snake_body[1:]:
        hold_position = turtle.position()
        turtle.goto(x = segment_position_memory[0], y = segment_position_memory[1])
        segment_position_memory = hold_position
    sleep(0.5)
    screen.update()

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


# What I need to do is create a user input system 
# where when I press 'W,' the first square moves upward,
# and the snake's body moves forward. In each iteration,
# the squares behind should follow the next one."

# while True:

# connect_movement(snake_body, 'w')

screen.listen()

screen.onkey(key='w', fun=lambda: connect_movement(snake_body, 'w'))
screen.onkey(key='s', fun=lambda: connect_movement(snake_body, 's'))
screen.onkey(key='a', fun=lambda: connect_movement(snake_body, 'a'))
screen.onkey(key='d', fun=lambda: connect_movement(snake_body, 'd'))



    # for turtle in snake_body:
    #     new_x =  turtle.position()[0]
    #     new_y = turtle.position()[1]
    #     turtle.goto(x= new_x + 20, y = new_y)



# turtle = Turtle()
# turtle.shape('square')



screen.exitonclick()
