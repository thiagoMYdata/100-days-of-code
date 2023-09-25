from random import randint

def player_input():
    player = input('What do you choose? Type 0 for  Rock, 1 for Paper or 2 for Scissors ')
    if player.isnumeric and player in ('0','1','2'):
        return int(player)
    elif player.lower() == 'end':
        return player
    else:
        while True:
            player = input('[ERROR] Wrong input try again!')
            if player.isnumeric and player in  ('0','1','2'):
                return int(player)
            elif player.lower() == 'end':
                return player
        

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock,paper,scissors]

while True:
    #print('What do you choose? Type 0 for  Rock, 1 for Paper or 2 for Scissors ', end='')
    player = player_input()
    if player == 'end': break
    
    computer = randint(0,2)

    print(f'{rps[player]}\nComputer choose\n{rps[computer]}\n\n')

    if player == computer:
        print(' YEP draw game')
    elif player == 0 and computer == 2 or player == 1 and computer == 0 or player == 2 and computer == 1:
        print('PLAYER WON\nPogU u did it!!') 
    else:
        print('COMPUTER WON\nU lost! maybe next time FeelsOkayMan')


