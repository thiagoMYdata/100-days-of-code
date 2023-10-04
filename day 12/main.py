#Number Guessing Game Objectives:
# Include an ASCII art logo. done
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
from random import randint

#print(logo)


def is_number(x):
    """
    try to convert x to float if fails return False and if succeed return True
    """
    try:
        int(x) 
        return True
    except ValueError:
        return False

def number_input():
    """
    This function is a loop that allows the user to choose a number between 1 and 100
    """
    number_guessed = input('Make a guess: ')

    if is_number(number_guessed):
        number_guessed = int(number_guessed)
        if number_guessed >= 1 and number_guessed <= 100:
            return number_guessed
        else:
            print('number out of range pls try again and make sure is between 1 and 100.')
            return number_input()
    else:
        print('Invalid input this\'s not a number')
        return number_input()

def life_system():
    difficulty_choose = input('Choose a difficulty. Type \'easy\' or \'hard\': ').lower()
    if difficulty_choose in ('easy','hard'):
        if difficulty_choose == 'easy':
            print('You have 10 attempts remaining to guess the number.\n')
            return 10
        elif difficulty_choose == 'hard':
            print('You have 5 attempts remaining to guess the number.\n')
            return 5
    else:
        print('Wrong input please try again.')
        return life_system()



secret_number = randint(1,100)
user_num =-1 # silly numbers 

print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100."""
)

life = life_system()

while life != 0 or secret_number != user_num:
    user_num = number_input()
    print(user_num)
    if user_num == secret_number:
        print(f'You got it! The answer was {secret_number}.')
        break
    elif user_num > secret_number:
        print(f"""Too high.
Guess again.
You have {life} attempts remaining to guess the number.""")
    else:
        print(f"""Too low.
Guess again.
You have {life} attempts remaining to guess the number.""")
    life -= 1

    if life == 0:
        print(f'L u lost Sadge the number was {secret_number}. If u wanna try again pls restart the script')
