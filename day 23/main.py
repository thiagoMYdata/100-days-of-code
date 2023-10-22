import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def build_object_list():
    cars_list = []
    for _ in range(20):
        car = CarManager()
        cars_list.append(car)
    return cars_list



# Configure Screen Method
screen = Screen()
screen.bgcolor('#4b494a')
screen.setup(width=600, height=600)
screen.tracer(0)

# calling class:
jimmy = Player()

scoreboard = Scoreboard()

cars_list = build_object_list()


# screen keys listen
screen.listen()
screen.onkeypress(key='w', fun=jimmy.up_press)
screen.onkeyrelease(key='w', fun=jimmy.stop)
screen.onkeypress(key='s', fun=jimmy.down_press)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()



    if jimmy.level_up():     ## level Up: reset cars, hide the previous cars and increase the speed
        for car in cars_list:
            car.clear_cars()
        scoreboard.level_increment()

        jimmy.new_level()

        if scoreboard.level <= 5:
            cars_list = build_object_list()
            for car in cars_list:
                car.move_by += car.move_increment


    for car in cars_list:     ## condition to lose
        if car.distance(jimmy) < 25:
            scoreboard.game_over()
            game_is_on = False

    for car in cars_list:     ## Cars move forward 
        car.move_forward()
        if car.xcor() < -320:
            car.restart_loop()


    if scoreboard.level > 5:   ## condition to win
        scoreboard.game_over()
        game_is_on = False
    



screen.exitonclick()
