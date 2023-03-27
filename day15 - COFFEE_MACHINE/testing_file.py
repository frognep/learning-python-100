from os import system
from drinks import MENU
from inventory import RESOURCES

def clear():
    system("cls")


selection = (MENU["espresso"]["ingredients"])

print(selection["water"])