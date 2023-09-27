from string import ascii_letters, digits
from random import choice,choices,shuffle

letters_num = int(input('How many letters would you like in your password? '))

symbols_num = int(input('How many symbols would you like? '))

numbers_num = int(input('How many numbers would you like? '))

symbols_string = '?!@#$&%*'

# logic

letters = choices(ascii_letters, k=letters_num)

symbols = choices(symbols_string, k=symbols_num)

numbers = choices(digits, k = numbers_num)

char_list = list(letters+symbols+numbers)
shuffle(char_list)
password = ''.join(char_list)

print(password)