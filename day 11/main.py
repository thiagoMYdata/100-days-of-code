############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.   <-- i choose this one

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################
#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run
#################################################
from art import logo
import random


def cards_logic(list_given):
    """
    cards_logic is how the code choose pick up a card base on a list of option witch is hand_options and then return the correct value
    """
    hand_options = list(range(2,10)) + [10]*3 + [11]
    hand = random.choice(hand_options)   
    if hand == 11:
        if  ( sum(list_given) + 11 <= 21):
            return 11

        elif sum(list_given) + 1 <= 21:
            return 1
    else:
        return hand


def user_action():
    """
    so this function randomize the cards that users/comp will pick up as long as the user want
    """
    global user_combo

    while len(user_combo) <= 1:
        user_combo.append(cards_logic(user_combo))
   
    print(f'Your cards: {user_combo}, current score: {sum(user_combo)}')

    
    if  sum(user_combo) == 21:
        return
    elif sum(user_combo) > 21:
        print('You went over.')
        return

    wanna_continue = input('Do u wanna pick up another card? press \'y\' or press \'n\' to stop ').lower()
    
    if wanna_continue == 'n':
        return
    else:
        user_combo.append(cards_logic(user_combo))
        user_action()


def comp_action():
    """
    so this function is the same as the user action + probability to make the computer play and add some random aspect to the game
    """
    global comp_combo


    if len(comp_combo) <= 1:    # first and second cards
        comp_combo.append(cards_logic(comp_combo))
    elif len(comp_combo) == 2 and ( random.choice([True,False,False]) or sum(comp_combo) <= 10): # third card
        comp_combo.append(cards_logic(comp_combo))
    elif random.choice([True,False,False,False]) or sum(comp_combo) <= 14:   # four card and plus
        comp_combo.append(cards_logic(comp_combo))
    # else:
    #     print(f'Computer\'s final hand: {comp_combo}, current score: {sum(comp_combo)}')

    if  sum(comp_combo) == 21:
        print(f'Computer\'s final hand: {comp_combo}, current score: {sum(comp_combo)}')
    elif sum(comp_combo) > 21:
        print('Opponent went over.')
        print(f'Computer\'s final hand: {comp_combo}, current score: {sum(comp_combo)}')
    elif sum(comp_combo) >= 17:
        print(f'Computer\'s final hand: {comp_combo}, current score: {sum(comp_combo)}')
    else:
        comp_action()

newgame ='y'

while newgame != 'n':
    print(logo)

    user_combo = []
    comp_combo = []


    user_action()


    comp_action()

    user_score = sum(user_combo) 
    comp_score =sum(comp_combo)

    # print(user_score,comp_score)

    if user_score == 21 and comp_score == 21:
        print('Draw, opponent has Blackjack and you also have Blackjack 😱')
    
    elif user_score == 21:
        print('Win with a Blackjack 😎')
    
    elif comp_score == 21:
        print('Lose, opponent has Blackjack 😱')

    elif user_score > 21 and comp_score > 21:
        print('You both guys went over 😤')
    
    elif user_score == comp_score:
        print('Draw you and your opponent have the same score i never saw this in my life wtf 😱')
    
    elif (user_score > comp_score and user_score < 21) or (user_score < comp_score and comp_score > 21):
        print('You win 😃')
    
    elif (user_score < comp_score and comp_score < 21) or (comp_score < user_score and user_score > 21):
        print('You lose 😃')

    
    newgame = input('Game Over! wanna play another one ( ͡~ ͜ʖ ͡° ) ? press \'y\' to play a new game or \'n\' to exit.: ').lower()[0]