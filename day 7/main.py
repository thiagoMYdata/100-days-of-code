from random import choice
from hangman_words import word_list
from hangman_art import logo


def user_guess_letter():
    global letter_guessed

    user_input = input('Guess a letter: ')

    while True:
        if user_input not in letter_guessed and len(user_input) == 1:
            return user_input
        user_input = input(f'What u used \'{user_input}\' as an entry is invalid! Try a new letter: ')

def stages_output(damege = -1):
    from hangman_art import stages
    global LIFE
    LIFE += damege
    print('-=+='*5 + '-')
    print(stages[LIFE])


print(logo)


LIFE = 6    ## stages[7] default

guess_word = choice(word_list)
guess_word_secret = guess_word
# guess_word = '_ '* (len(guess_word)-1) + '_'

guess_word = '_' * len(guess_word)

letter_guessed = []

print(guess_word_secret)

while True:
    try_this_letter = user_guess_letter()
    letter_guessed.append(try_this_letter)

    if try_this_letter in guess_word_secret:
        stages_output(damege=0)
        for i in range(len(guess_word_secret)):
            if try_this_letter == guess_word_secret[i]:
                guess_word = guess_word[:i] + try_this_letter + guess_word[i + 1:]
        print(' '.join(guess_word))
    else:
        stages_output()
        print(' '.join(guess_word))

    if LIFE ==  0:
        print(f'Maybe next time FeelsOkayMan. The word was {guess_word_secret}')
        break

    if guess_word == guess_word_secret:
        print('U did it congrats!')
        break

