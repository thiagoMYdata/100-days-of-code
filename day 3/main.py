def choice(*args):
    while True:
        answer = input()
        if answer in args:
            return answer
        else:
            print(f'Invalid answer try {args}')

print('''
*******************************************************************************\n\
         |                   |                  |                     |\n\
_________|________________.=""_;=.______________|_____________________|________ \n\
|                   |  ,-"_,=""     `"=.|                  | \n\
|___________________|__"=._o`"-._        `"=.______________|___________________ \n\
         |                `"=._o`"=._      _`"=._                     | \n\
_________|_____________________:=._o "=._."_.-="'"=.__________________|________ \n\
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   | \n\
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________\n\
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              | \n\
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______ \n\
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   | \n\
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________\n\
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____ \n\
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_\n\
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____ \n\
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ \n\
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____ \n\
/______/______/______/______/______/______/______/______/______/______/_____ /_\n\
*******************************************************************************
''')

print(
'Welcome to the Tresure Island\n\
Your mission is to find the treasure.')

print('You\'re at a cross road. Where do you want to go? Type "left" or "right"')
answer = choice('right','left')
if answer == 'left':
    print('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
    answer = choice('wait','swim')
    if answer == 'wait':
        print('You arrive at the  island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?')
        answer = input().lower()
        if answer == 'yellow':
            print('You found the treasure! You Win!')
        elif answer == 'red':
            print('It\'s a room full of fire. Game Over.')
        elif answer == 'blue':
            print('You enter a room of beasts. Game Over.')
        else:
            print('You chose a door that doesn\'t exist. Game Over.')
    else:
        print('You get attacked by an angry trout. Game Over.')
else:
    print('You fell into a hole. Game Over.')
