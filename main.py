from imgs import logo
from data import MENU, resources
import os, platform

drink_options = {
    "1": "espresso",
    "2": "latte",
    "3": "cappuccino"
}


water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0



class Colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    ORANGE = '\033['
    RESET = '\033[0m' # Resets color to terminal's default


while True:
    def shutdown():
        global money

        if money > 0:
            print(f"\nDispensing your change of ${money}...")
            print(f"Thank you for choosing Munchn' Donuts")
            return False
        else:
            print("\nThank you for choosing Munchn' Donuts")
            return False

    def remaining_balance():
        global money

        if money < MENU['espresso']['cost']:
            print(f"{Colors.RED}Funds available: ${money}{Colors.RESET}  |  Add quarters to begin")
        else:
            print(f"{Colors.BLUE}Funds available: ${money}{Colors.RESET}")

    def add_coins():
        global money

        print("\n" *50)
        print(logo)
        print(f"{Colors.BLUE}Add Coins{Colors.RESET}\n")

        quarter_amt = int(input("How many quarters would you like to add? "))

        money += .25 * quarter_amt

    def report():
        print("\n" *50)
        print(logo)
        print(f"{Colors.BLUE}Report:\n{Colors.RESET}")
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")
        print("\n")

        back_to_menu = input("ENTER to go back to menu: \n")

    def menu(choice):
        global money
        global water
        global coffee
        global milk

        if choice == "1":
            if validate(choice):
                print(f"\n\nPreparing your {selected_drink}. Enjoy!\n")

                money -= MENU['espresso']['cost']
                water -= MENU['espresso']['ingredients']['water']
                coffee -= MENU['espresso']['ingredients']['coffee']

                back_to_menu = input("ENTER to return to menu ").lower()

        elif choice == "2":
            if validate(choice):
                print(f"\n\nPreparing your {selected_drink}. Enjoy!\n\n")

                money -= MENU['latte']['cost']
                water -= MENU['latte']['ingredients']['water']
                milk -= MENU['latte']['ingredients']['milk']
                coffee -= MENU['latte']['ingredients']['coffee']

                back_to_menu = input("ENTER to return to menu ").lower()

        elif choice == "3":
            if validate(choice):
                print(f"\n\nPreparing your {selected_drink}. Enjoy!\n\n")

                money -= MENU['cappuccino']['cost']
                water -= MENU['cappuccino']['ingredients']['water']
                milk -= MENU['cappuccino']['ingredients']['milk']
                coffee -= MENU['cappuccino']['ingredients']['coffee']

                back_to_menu = input("ENTER to return to menu ").lower()

    def validate(drink):
        drink = drink_options[choice]
        cost = MENU[drink]['cost']
        ingredients = MENU[drink]['ingredients']
        # milk = MENU[drink]['ingredients']['milk']
        errors = []

        # check money
        if cost > money:
            errors.append("Insufficient funds for this drink.")

        # check milk
        if "milk" in ingredients:
            if MENU[drink]['ingredients']['milk'] > resources["milk"]:
                errors.append(f"Not enough milk to make this drink.")

        # check water
        if MENU[drink]['ingredients']['water'] > resources["water"]:
            errors.append(f"Not enough water to make this drink.")

        # if there are errors, show them
        if errors:
            print("\n" * 50)
            print(f"\n{Colors.RED}Unable to process order.{Colors.RESET}")
            for error in errors:
                print(f"- {error}")
            back_to_menu = input("\nENTER to go back to menu: ")
            return False

        return True

    print("\n" *50)
    print(logo)
    remaining_balance()
    print("\nPlease make a selection\n")
    print("1. Espresso | $1.50\n2. Latte | $2.50\n3. Cappuccino | $3.00\n-\nC. Add Coins\nX. Exit")

    choice = input("\nType your selection: ").lower()

    if choice in drink_options:
        selected_drink = drink_options[choice]

    if choice == "report":
        report()
    elif choice == "c":
        add_coins()
    elif choice == "x":
        shutdown()
        break
    else:
        menu(choice)
