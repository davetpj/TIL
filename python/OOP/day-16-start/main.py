from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    options = menu.get_items()
    user_decided = input(f"What would you like? ({options}):")
    print(user_decided)

    if user_decided == "off":
        break
    elif user_decided == "report":
        # show current resources
        coffee_maker.report()
        money_machine.report()
    elif user_decided in menu.get_items():
        drink = menu.find_drink(user_decided)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        print("error")

