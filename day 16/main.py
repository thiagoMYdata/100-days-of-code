from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f'What you u like to order ({options})')

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink=drink) and  money_machine.make_payment(cost=drink.cost):
            coffe_maker.make_coffee(drink)

# coffe_maker.report()

# money_machine.report()

# # a = input('What would you like? (ESPRESSO/LATTE/CAPPUCCINO): ').lower()
# # print(Menu.get_items(self=a))

# a = input('What would you like? (ESPRESSO/LATTE/CAPPUCCINO): ')

# menu_item = MenuItem(name=a, )



# menu_item.name = input('What would you like? (ESPRESSO/LATTE/CAPPUCCINO): ').lower()

# print(coffe_maker.is_resource_sufficient(menu_item.name))

# print(MenuItem.cost)



menu = Menu()

print(menu.get_items())