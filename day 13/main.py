############DEBUGGING#####################
# # Describe Problem
"""
the issue is "i" will never reach 20 and "if i == 20:" never gonna happen bc range(0,20) == [0,1,2,...,17,18,19]
solution just change "for i in range(0, 20):" to  "for i in range(0,21)"   
"""
# def my_function():
#   for i in range(0, 20):      # range  => start from 0 and end in 20 (step == 1)
#     if i == 20:               # i == 0
#       print("You got it")
# my_function()

# Reproduce the Bug
"""
so the problem this time is randint choose a number between 1 and 6 and dice_imgs index goes from 0 to 5 that why indexError, dice_imgs[6] doesn't exist
solution is to change randint(1,6) to randint(0,5) bc the element 0 hasn't had a chance to be called also
"""
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)                    # IndexError: list index out of range
# print(dice_imgs[dice_num])

# Play Computer
"""the year 1994 doens't have a output so we need to fix it just change the line 
"if year > 1980 and year < 1994:" to "if year > 1980 and year <= 1994:" and now 1994 have the "You are millenial." output
"""
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# Fix the Errors
"""
age was str and i change to int using int()
print(...) was in the wrong indentation just press TAB one time or space 4 times
print("You can drive at age {age}.") the only sintax error here is that this string is not a fstring so we just have to convert and every thing will work just fine
"""
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")


#Print is Your Friend
"""
print(pages, word_per_page) ==output==> pages 0 
so the problem is == instead of =
so the line word_per_page == int(input("Number of words per page: ")) return False instead of the user input()
the correct line is word_per_page = int(input("Number of words per page: ")) to assign the user input() to word_per_page
"""
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# print(pages,word_per_page)
# total_words = pages * word_per_page
# print(total_words)


#Use a Debugger
"""
https://pythontutor.com/render.html#mode=display
the code is fine the only problem is b_list.append(new_item) is in the wrong indentation 2 space instead of 4 or 1 tab
"""
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])



# # Extra
# # Which number do you want to check?

# number = int(input('Tell me a number '))

# if number % 2 == 0:
#     print('This is an even number.')

# else:
#     print('This is an odd number')




# Which year do you want to check?
# year = int(input())

# if year % 4 == 0:
#     if year % 100:
#         if year % 400 == 0:
#             print('Leap year')
#         else:
#             print('Not leap year.')
#     else:
#         print('Leap year')
# else:
#     print('Not leap year.')



# # Target is the number up to which we count
# target = int(input('era pra não ter nada aqui mas tem'))
# for number in range(1, target + 1):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
