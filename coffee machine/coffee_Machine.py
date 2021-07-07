from data import MENU, resources

profit = 0

working = True


def is_resource_sufficient(order_ingredients):
    # {water:50, coffee:18}
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def calculate_remain(order_ingredients):
    for item in order_ingredients:
        resources[item] = resources[item] - order_ingredients[item]


def progress_coins():
    print("please insert coins.")
    total = int(input("how many 1 lira:"))
    total += int(input("how many 50 kuruş:")) * 0.5
    total += int(input("how many  25kuruş:")) * 0.25
    total += int(input("how many 10 kuruş:")) * 0.1
    total += int(input("how many 5 kuruş:")) * 0.05
    total += int(input("how many 1 kuruş:")) * 0.01
    return total


def buy_action():
    global profit
    print(f"you have ₺{user_deposit - drink['cost']} return")
    profit += drink['cost']
    calculate_remain(drink["ingredients"])


while working:
    asking = input("What would you like? (espresso/latte/cappuccino):   ")
    if asking == "off":
        working = False
    elif asking == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
        print(f"money: ₺{profit}")
    else:
        print(f"you ordered {asking}")
        drink = MENU[asking]
        if is_resource_sufficient(drink["ingredients"]):
            user_deposit = progress_coins()
            if user_deposit >= drink['cost']:
                buy_action()
            else:
                print(f"you need to deposit {drink['cost'] - user_deposit} euro more to have {asking}")
                choice = input("Add to money press continue or cancel to have your money back:").lower()
                if choice == 'cancel':
                    print("this is your money.")
                elif choice == "continue":
                    while user_deposit < drink['cost']:
                        user_deposit_new = progress_coins()
                        user_deposit = user_deposit + user_deposit_new
                        if user_deposit < drink['cost']:
                            print(f"you need to deposit {drink['cost'] - user_deposit} euro more to have {asking}")
                    buy_action()



