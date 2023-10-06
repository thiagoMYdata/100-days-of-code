# "Higher or Lower" is a simple guessing game  The objective of the game is to guess
#  whether the next one will be higher or lower than the current one.

# print(logo) de art.py

# import the game_data.py

# game logic: choose two randoms option on game_data => make the user decide who is the higher between the two options
    # if he chooses right then delete the lower option from the list and make the computer choose another word to compare
        # if, by some miracle the user finishes the game than there has to be a special message. surely i will do that in the next update
    # if he choose wrong than end the game with a message

from game_data import data
from random import choices, choice
from art import logo, vs



def print_func(list_index:list, mydata, score):
    print(logo)
    if score != 0: print(f'You\'re right! Current score: {score}.')
    print(f"{mydata[list_index[0]]['follower_count']}    Compare A: {mydata[list_index[0]]['name']}, {mydata[list_index[0]]['description']}, from {mydata[list_index[0]]['country']}")
    print(vs)
    print(f"{mydata[list_index[1]]['follower_count']}    Compare B: {mydata[list_index[1]]['name']}, {mydata[list_index[1]]['description']}, from {mydata[list_index[1]]['country']}")
    return

def user_input():
    x = input('Who has more followers? Type \'A\' or \'B\': ').upper()
    while not (x in ('A','B')):
        x = input('Please TO CHOOSE TYPE \'A\' OR \'B\': ').upper()
    if x == 'A':
        return 0
    else:     
        return 1


def higher_or_lower(list_index:list, mydata):
    score = 0
    index_avaiable = list(range(len(mydata)))
    if list_index == []:
        list_index = choices(index_avaiable , k=2)

    while True:
        print_func(list_index, mydata , score)

        user_choice = user_input()

        # max_value =  max([mydata[z]['follower_count'] for z  in list_index  ])

        max_value =  max([mydata[z]['follower_count'] for z  in list_index  ])

        if mydata[list_index[user_choice]]['follower_count'] == max_value:
            score += 1
            a, b = list_index[0], list_index[1]
            print(a,b)
            if a == list_index[user_choice]:
                list_index.remove(b)
                index_avaiable.remove(b)
            elif b == list_index[user_choice]:
                list_index.remove(a)
                index_avaiable.remove(a)
            else:
                print('tem algo de errado aqui')
        else:
            print(f'Sorry, that\'s wrong. Final score: {score}')
            return
        list_index.append(choice(index_avaiable))
 #       list_index.append(choice(range(len(mydata))))


mydata = data
list_index = []

higher_or_lower(list_index, mydata)