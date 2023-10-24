# file = open(r"C:\Users\Thiago\Desktop\2023\VS code\100 days of code\day 24\open write read\my_file.txt")
# contents = file.read()
# file.close()
# print(contents)


# with open(r"C:\Users\Thiago\Desktop\2023\VS code\100 days of code\day 24\open write read\my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# with open(r"C:\Users\Thiago\Desktop\2023\VS code\100 days of code\day 24\open write read\my_file.txt", mode= 'a') as file:
#     file.write('\nNew text.')



with open(r"C:\Users\Thiago\Desktop\2023\VS code\100 days of code\day 24\open write read\new_file.txt", mode= 'w') as file:
    file.write('\nNew text.')
