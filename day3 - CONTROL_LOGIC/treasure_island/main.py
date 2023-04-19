# 09/05/22
import logo_art

print(logo_art.chest)

# experimented with C++ style indentation
initial_message = (
    "Welcome to Treasure Island.\n"
    "Your mission is to find the treasure\n"
    "Two paths opens up."
)

print(initial_message)

path_choice = input(
    "The left path looks safer, but is three times as long as the right path.\nThe right path looks like it would be substantially quicker, yet more treacherous and rugged.\nLeft or right? ".lower()
)

if path_choice == "right":
    print()
    swim_choice = input(
        "You have navigated the path, only to stop at a high flow stream.\nSwim or wait? ".lower()
    )
    if swim_choice == "wait":
        print()
        door_choice = input(
            "The currents have slowed down, enabling you to cross the river safely.\nThree colored doors have appeared out of thin air.\nwhich door? Red, blue, or yellow? ".lower()
        )
        if door_choice == "red":
            print("You have been burned by fire!\nGame Over.")
        elif door_choice == " yellow":
            print("You Win !")
        elif door_choice == "blue":
            print("A blizzard has overcomed you, you have became frozen.\nGame Over.")
        else:
            (print("You did not choose a door. Game Over."))
    else:
        print("You have been swept away by the current..!\nGame Over.")
else:
    print("You have sunken into quicksand with no utility rope.\nGame Over.")