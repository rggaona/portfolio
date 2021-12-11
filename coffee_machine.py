import math

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# TODO: 1. INPUT DE COFFEE
# TODO: 2. REPORT
# TODO: 3. CHECK RESOURCES
# TODO: 4. PROCESS COIN
# TODO: 5. CHECK TRANSACTION
# TODO: 6. MAKE COFFEE

continue_program = True


def check_resources(coffee):
    if coffee == "espresso":
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    elif coffee == "latte" or coffee == "cappuccino":
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]


def process_coin(quarters, dimes, nickels, pennies):
    total = quarters * 0.25
    total += (dimes * 0.10)
    total += (nickels * 0.05)
    total += (pennies * 0.01)
    return total


def sufficient_resources(coffee_ingredients):
    for item in MENU[coffee_ingredients]["ingredients"]:
        if MENU[coffee_ingredients]["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def compare(price):
    total = process_coin(costumer_quarter, costumer_dimes, costumer_nickels, costumer_pennies)
    if total > price:
        change = round((total - price), 2)
        check_resources(coffee_choice)
        resources["money"] += MENU[coffee_choice]["cost"]
        return f"Here is ${change} in change\nHere is your {coffee_choice} ☕️. Enjoy!"
    elif total < price:
        return "Sorry, that's not enough money. Money refunded"


while continue_program:
    coffee_choice = input("What would you like? (espresso, latte, cappuccino): ")
    coffee_options = ["espresso", "latte", "cappuccino"]
    if coffee_choice == "off":
        continue_program = False
    elif coffee_choice == "report":
        print(f"Water: {resources['water']}ml.")
        print(f"Milk: {resources['milk']}ml.")
        print(f"Coffee: {resources['coffee']}g.")
        print(f"Money: ${resources['money']}.")
    elif coffee_choice in coffee_options:
        if sufficient_resources(coffee_choice):
            print("Please insert coins.")
            costumer_quarter = int(input("How many quarters?: "))
            costumer_dimes = int(input("How many dimes?: "))
            costumer_nickels = int(input("How many nickels?: "))
            costumer_pennies = int(input("How many pennies?: "))
            print(compare(MENU[coffee_choice]["cost"]))
