menu = {
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
}

is_work = True
money = 0.00
resources_ok = True
total_coines = False


def coines():
    global resources_ok, total_coines, money
    coines_set = {
        "quaters": 0.25,
        "dimes": 0.10,
        "nickeles": 0.05,
        "pennies": 0.01,
    }
    off_coines = (input("Please, type 'coines' to star insert your coines or type 'off' to exit ")).lower()
    if off_coines != "off":
        quaters_quontities = int(input("How match quaters you insert:  "))
        total_quaters = coines_set["quaters"] * quaters_quontities
        dimes_quontities = int(input("How match dimes you insert:  "))
        total_dimes = coines_set["dimes"] * dimes_quontities
        nickeles_quontities = int(input("How match nickeles you insert:  "))
        total_nickeles = coines_set["nickeles"] * nickeles_quontities
        pennies_quontities = int(input("How match pennies you insert:  "))
        total_pannies = coines_set["pennies"] * pennies_quontities
        total = round((total_quaters + total_dimes + total_nickeles + total_pannies), 2)
        if total < menu[user_choice]["cost"] and total > 0:
            print("“Sorry that's not enough money. Money refunded")
            total_coines = False
        else:
            if total > menu[user_choice]["cost"]:
                total_change = round((total - menu[user_choice]["cost"]), 2)
                total = menu[user_choice]["cost"]
                print(f"Here is ${total_change} dollars in change.")
            total_coines = True
            money += total
    else:
        total_coines = False
        resources_ok = False
#   return total_coines, resourses_ok


def check_resources():
    global resources_ok
    water = menu[user_choice]["ingredients"]["water"]
    water_storage = resources["water"]
    try:
        milk = menu[user_choice]["ingredients"]["milk"]
        milk_storage = resources["milk"]
        if milk < milk_storage:
            resources_milk = True
    #        print("resources_milk ", resources_milk)
        else:
            print("Sorry not enough milk")
            resources_milk = False
    #        print("resources_milk: ", resources_milk)
    except:
        resources_milk = None
    coffee = menu[user_choice]["ingredients"]["coffee"]
    coffee_storage = resources["coffee"]
    if water < water_storage:
        resources_water = True
    #    print("resources_water: ", resources_water)
    else:
        print("Sorry not enough water")
        resources_water = False
    #    print("resources_water: ", resources_water)
    if coffee < coffee_storage:
        resources_coffee = True
    #    print("resources_coffee: ", resources_coffee)
    else:
        print("Sorry not enough coffee")
        resources_coffee = False
    #    print("resources_coffee: ", resources_coffee)
    if resources_coffee == True and resources_water == True:
        if resources_milk == True or resources_milk == None:
            resources_ok = True
    else:
        resources_ok = False
#   return resources_ok


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money} ")


def make_coffee():
#    report()
    resources["water"] -= menu[user_choice]["ingredients"]["water"]
    try:
        resources["milk"] -= menu[user_choice]["ingredients"]["milk"]
    except:
        pass
    resources["coffee"] -= menu[user_choice]["ingredients"]["coffee"]
    print(f"Here is your {user_choice}. Enjoy!")
#    report()


while is_work:
    user_choice = input("What woud you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        print("mashine turn off")
        is_work = False
    elif user_choice == "report":
        report()
    elif user_choice == "latte":
        check_resources()
        if resources_ok == True:
            coines()
            if total_coines == True:
                make_coffee()
    elif user_choice == "espresso":
        check_resources()
        if resources_ok == True:
            coines()
            if total_coines == True:
                make_coffee()
    elif user_choice == "cappuccino":
        check_resources()
        if resources_ok == True:
            coines()
            if total_coines == True:
                make_coffee()
