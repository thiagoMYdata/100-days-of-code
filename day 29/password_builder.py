from string import ascii_letters, digits
from random import choice,choices,shuffle


def builder():
    symbols_string = '?!#&%'

    # logic
    letters = choices(ascii_letters, k=6)
    symbols = choices(symbols_string, k=1)
    numbers = choices(digits, k = 2)

    char_list = list(letters+symbols+numbers)
    shuffle(char_list)

    password = ''.join(char_list)

    return password
