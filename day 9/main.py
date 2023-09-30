from art import logo
def biggest_bid(name:str, bid:int):
    global dic
    # if dic == None:
    #     dic = {}
    dic[name] = bid

    values = dic.values()

    memory = {key:valor for key,valor in dic.items() if valor == max(values)}
    return memory

dic = {}


print(logo)
print('Welcome to the secret auction program.')

while True:
    name = input('What is your name?: ')
    bid = int(input('What\'s your bid?: $'))
    memory = biggest_bid(name, bid)
    other_bidders = input('Are there any other bidders? Type \'yes\' or \'no\'.').lower()
    if other_bidders == 'no':
        if len(list(memory.keys())) > 1:
            print(f'The winners are: {list(memory.keys())} and they bid ${list(memory.values())[0]}')
        else:
            print(f'The winner is {list(memory.keys())} and the bid was ${list(memory.values())[0]}')
        break