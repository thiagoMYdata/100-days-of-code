# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# # import pandas
# # student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.




import pandas as pd

data = pd.read_csv(r'100 days of code\day 26\nato_phonetic_alphabet.csv')


letter_code_dict = {row.letter:row.code for _, row in data.iterrows()}     ## The best part of the entire code is iterrows()

user_word = input('Tell me a word to convert into code language: ').strip().upper()

language_to_code = [letter_code_dict[letter] for letter in user_word ]

print(language_to_code)

