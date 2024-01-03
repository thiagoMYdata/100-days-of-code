import pandas as pd

# def check_if_have_numbers(string):
#     while True:
#         if string == '':
#             return False
#         try:
#             int(string[0])
#         except ValueError:

#             string = string[1:]
#         else:
#             return True


data = pd.read_csv(r'100 days of code\day 30\NATO CODE\nato_phonetic_alphabet.csv')


letter_code_dict = {row.letter:row.code for _, row in data.iterrows()}     ## The best part of the entire code is iterrows()



# print(check_if_have_numbers(user_word))


def generate_phonetic():
    user_word = input('Tell me a word to convert into code language: ').strip().upper()
    try:
        language_to_code = [letter_code_dict[letter] for letter in user_word ]
    except KeyError:
        print('opss please type only letter. TRY AGAIN')
        generate_phonetic()
    else:
        print(language_to_code)


generate_phonetic()

