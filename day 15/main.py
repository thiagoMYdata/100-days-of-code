# TODO: 2. Check resources sufficient to make drink order.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            'milk':0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 400,
    "milk": 300,
    "coffee": 100,
}

# TODO: 1. print report of all coffee machine resources

# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

def user_input():
    answer = input('What would you like? (ESPRESSO/LATTE/CAPPUCCINO): ').lower()
    if answer in ('espresso', 'latte', 'cappuccino', 'off', 'report'):
        return answer
    else: 
        print('Please try again')
        return user_input()

def money_sum(MENU:dict,drink_choice ):
    price = MENU[drink_choice]['cost']
    quarters    = float(input('How many quarters (twenty five cents): '))
    dimes       = float(input('How manu dimes (10 cents): '))
    nickles     = float(input('How many nickles (5 cents):'))
    pennies     = float(input('How many pennies (1 cent):'))
    coins = round(sum([quarters*0.25,dimes*0.1, nickles*0.05,pennies*0.01]),2)
    change_amount = coins - price
    if change_amount > 0:
        return change_amount
    elif change_amount == 0 :
        return 'NaN change_amount'

def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def check_resources(resources:dict, MENU:dict, drink_choice):
    if drink_choice in MENU:
        drink_opt = list(MENU[drink_choice]['ingredients'].values())
        resources_available = list(resources.values())
        result = [resources_available[j] - drink_opt[j] for j in range(len(resources_available))]
        if min(result) >= 0:
            return result
        else: 
            return 'insufficient resources'
    else:
        return 'Invalid drink choice'

def coffee_machine_logic(resources:dict, MENU:dict):
    drink_choice = user_input()

    if drink_choice == 'off':
        print('shutdown machine.exe...')
        return
    elif drink_choice == 'report':
        print(resources)
        return coffee_machine_logic(resources=resources, MENU=MENU)
    
    result = check_resources(resources=resources, MENU=MENU, drink_choice=drink_choice)

    if not (result == 'insufficient resources'):
        print('please insert coins.')

        change_amount = money_sum(MENU=MENU,drink_choice=drink_choice)

        if is_number(change_amount):
            print(f'Here is ${change_amount} in change.')

        dict_keys = resources.keys()
        for keys, value in zip(dict_keys, result):
            resources[keys] = value

        print(f'Here is your {drink_choice} ☕️. Enjoy!')

    elif result == 'insufficient resources':
        print('​Sorry there is not enough resources.')
        return
    return coffee_machine_logic(resources=resources, MENU=MENU)
    
coffee_machine_logic(resources=resources, MENU=MENU)


    
# print(list(MENU['latte']['ingredients'].values()))