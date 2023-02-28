from os import system
from drinks import MENU
from inventory import RESOURCES

# NOTE:: I know I could have added a check for sufficient resources function but 
# I decided to leave my code as-is as it is what I came up with initially.
# I want to be able to see my progression in learning and improving.


def clear():
    system("cls")

# user-payment function
def insertCoins():
    print("Please insert coins.")
    quarterWorth = 0.25
    dimeWorth = 0.10
    nickelWorth = 0.05
    pennyWorth = 0.01
    
    quarterAmount = int(input("How many quarters?: "))
    dimeAmount = int(input("How many dimes?: "))
    nickelAmount = int(input("How many nickels?: "))
    pennyAmount = int(input("How many pennies?: "))

    quarterCalculation = quarterWorth * quarterAmount
    dimeCalculation = dimeWorth * dimeAmount
    nickelCalculation = nickelWorth * nickelAmount
    pennyCalculation = pennyWorth * pennyAmount

    totalUserCoins = quarterCalculation + dimeCalculation + nickelCalculation + pennyCalculation

    return totalUserCoins

# user-change function
def changeCalculation(pay, itemCost):
    userChange = pay - itemCost

    return round(userChange, 2)

# prints report of current resources
def printReport():
    print(f"Water: {waterAmount}ml\n"
          f"Milk: {milkAmount}ml\n"
          f"Coffee: {coffeeAmount}g\n"
          f"Money: ${moneyAmount}\n")

# checks if there are sufficient ingredients [[ NOT PROGRAMED]]
def inventoryCheck():
    print("test")

clear()

# starting resources for the day
waterAmount = RESOURCES["water"]
milkAmount = RESOURCES["milk"]
coffeeAmount = RESOURCES["coffee"]
moneyAmount = 0

loopSwitch = True
while loopSwitch:
    userSelection = input(" What would you like? (espresso/latte/cappuccino): ").lower()

    # break out of while-loop
    if userSelection == "off":
        loopSwitch = False

    elif userSelection == "report":
        printReport()
        
    # output inventory report
    else:
        userItemCost = MENU[f"{userSelection}"]["cost"]

    # drink selection conditions
    if userSelection == "espresso":
        userItemWater = MENU[f"{userSelection}"]["ingredients"]["water"]
        userItemCoffee = MENU[f"{userSelection}"]["ingredients"]["coffee"]
        userPay = insertCoins()
        userChange = changeCalculation(userPay, userItemCost)
        if userPay < userItemCost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            if userItemWater > waterAmount:
                print("Sorry there is not enough water.")
            elif userItemCoffee > coffeeAmount:
                print("Sorry there is not enough coffee.")
            else:
                waterAmount -= userItemWater
                coffeeAmount -= userItemCoffee
                moneyAmount += MENU[f"{userSelection}"]["cost"]
                print(f"Here is ${userChange} in change!")
                print("Here is your espresso ☕. Enjoy!")
                
    elif userSelection == "latte":
        userItemWater = MENU[f"{userSelection}"]["ingredients"]["water"]
        userItemCoffee = MENU[f"{userSelection}"]["ingredients"]["coffee"]
        userItemMilk = MENU[f"{userSelection}"]["ingredients"]["milk"]
        userPay = insertCoins()
        userChange = changeCalculation(userPay, userItemCost)
        if userPay < userItemCost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            if userItemWater > waterAmount:
                print("Sorry there is not enough water.")
            elif userItemCoffee > coffeeAmount:
                print("Sorry there is not enough coffee.")
            elif userItemMilk > milkAmount:
                print("Sorry there is not enough milk.")
            else:
                waterAmount -= userItemWater
                coffeeAmount -= userItemCoffee
                moneyAmount += MENU[f"{userSelection}"]["cost"]
                print(f"Here is ${userChange} in change!")
                print("Here is your latte ☕. Enjoy!")

    elif userSelection == "cappucino":
        userItemWater = MENU[f"{userSelection}"]["ingredients"]["water"]
        userItemCoffee = MENU[f"{userSelection}"]["ingredients"]["coffee"]
        userItemMilk = MENU[f"{userSelection}"]["ingredients"]["milk"]
        userPay = insertCoins()
        userChange = changeCalculation(userPay, userItemCost)
        if userPay < userItemCost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            if userItemWater > waterAmount:
                print("Sorry there is not enough water.")
            elif userItemCoffee > coffeeAmount:
                print("Sorry there is not enough coffee.")
            elif userItemMilk > milkAmount:
                print("Sorry there is not enough milk.")
            else:
                waterAmount -= userItemWater
                coffeeAmount -= userItemCoffee
                moneyAmount += MENU[f"{userSelection}"]["cost"]
                print(f"Here is ${userChange} in change!")
                print("Here is your cappuccinno ☕. Enjoy!")
    

# TO-DO
# reduce some repeated code into a function