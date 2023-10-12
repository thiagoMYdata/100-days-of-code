from turtle import Turtle, Screen, mainloop

turtle = Turtle()
turtle.speed(0)

def press_w():
    turtle.forward(10)
    

def press_s():
    turtle.backward(10)

def press_a():
    turtle.left(10)

def press_d():
    turtle.right(10)

def press_c():
    turtle.reset()


screen = Screen()


screen.listen()

screen.onkeypress(key='w', fun=press_w)
screen.onkeypress(key='s', fun=press_s)
screen.onkeypress(key='a', fun=press_a)
screen.onkeypress(key='d', fun=press_d)

screen.onkey(key='c', fun=press_c)





screen.exitonclick()
