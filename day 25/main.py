import turtle
import pandas as pd
from write_state import WriteState
from time import sleep


## setting screen from turtle
screen = turtle.Screen()
screen.title('US States Game')
img = r'100 days of code\day 25\blank_states_img.gif'
screen.addshape(img)
screen.setup(width=725, height=491)

turtle.shape(img)

## get x and y coordinates to place the exactly label 
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)



state_db = pd.read_csv(r'100 days of code\day 25\50_states.csv')
names = state_db.state.to_list()


write_state = WriteState()

game_state = True
state_count = 0
guessed_states = []


while state_count <= 50 or game_state == True:
    
    answer_state = screen.textinput(title=f'{state_count}/50 States Correct ', prompt='What\'s another state\'s name?').title().strip()



    if answer_state in names and answer_state not in guessed_states:
        tuple_results   = state_db[state_db.state == answer_state].to_records(index=False)[0]
        write_state.write_to(tuple_results)
        
        guessed_states.append(answer_state)
        
        state_count +=1

    if answer_state == 'Exit':
        missed_states = [state for state in names if state not in guessed_states]
        # missed_answer = state_db[state_db.state == missed_states].to_records(index=False)
        missed_answer = state_db[state_db['state'].isin(missed_states)].to_records(index=False)

        # print(missed_answer)
        for index in range(len(missed_states)):
            write_state.check_missed_states(missed_answer[index])
        sleep(5)
        game_state = False
        break

# turtle.mainloop()


