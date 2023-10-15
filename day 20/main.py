from turtle import Turtle, Screen


# screen configuration
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('My_Snake_Game')
screen.tracer(0)


class SnakeLogic:
    def __init__(self):
        self.snake_body = []
        self.control_options = {'w': ['a','d'],  'a':['s','w'], 's':['d','a'], 'd':['w','s']}
        self.control = 'd'
    # d u can use w == 90 or s == 270 
    # w u can use a == 90 or d == 270
    # a u can use w == 270 or s == 90
    # s u can use a == 270 or d == 90


    def create_snake(self):
        # start snake body
        x_options = range(0, -120, -20 )
        for i in range(5):
            new_turtle = Turtle(shape='square')
            new_turtle.up()
            new_turtle.color('#393')
            new_turtle.goto(x= x_options[i], y=0)
            screen.update()
            self.snake_body.append(new_turtle)

    def head_movement(self,direction):
        head =  self.snake_body[0]
        position = head.position()

        self.control_options

        if direction == self.control_options[self.control][0]:
            head.left(90)
            head.forward(10)
            self.control = direction
            return position
        elif direction == self.control_options[self.control][1]:
            head.right(90)
            head.forward(10)
            self.control = direction
            return position
        elif direction == 'forward':
            head.forward(10)
            return position
        # else:
        #     return 'There_is_nothing_to_be_done_here '

    def connect_movement(self, direction):
        from time import sleep
        # snake_body.reverse()
        segment_position_memory = self.head_movement( direction)
        # for _ in len(snake_body) - 1:
        for turtle in self.snake_body[1:]:
            hold_position = turtle.position()
            turtle.goto(x = segment_position_memory[0], y = segment_position_memory[1])
            segment_position_memory = hold_position
        # sleep(0.01)
        screen.update()
    def go_forward(self):
        from time import sleep
        self.connect_movement('forward')
        sleep(0.1)

game = SnakeLogic()
game.create_snake()
# game.head_movement()
# game.connect_movement()




# print(snake_body) # print a object list


# What I need to do is create a user input system 
# where when I press 'W,' the first square moves upward,
# and the snake's body moves forward. In each iteration,
# the squares behind should follow the next one."

# while True:

# connect_movement(snake_body, 'w')

screen.listen()

screen.onkey(key='w', fun=lambda: game.connect_movement( 'w'))
screen.onkey(key='s', fun=lambda: game.connect_movement( 's'))
screen.onkey(key='a', fun=lambda: game.connect_movement( 'a'))
screen.onkey(key='d', fun=lambda: game.connect_movement( 'd'))

while True:
    game.go_forward()

    # for turtle in snake_body:
    #     new_x =  turtle.position()[0]
    #     new_y = turtle.position()[1]
    #     turtle.goto(x= new_x + 20, y = new_y)



# turtle = Turtle()
# turtle.shape('square')



screen.exitonclick()
