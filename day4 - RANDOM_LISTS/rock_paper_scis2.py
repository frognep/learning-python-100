rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

wep_Choice = [rock, paper, scissors]
wep_Random = random.randint(0, len(wep_Choice) - 1)
wep_Computer = wep_Choice[wep_Random]

user_Input = int(input("What do you choos? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

# invalid inputs are checked first, rest of code runs after else statement
if user_Input >= 3 or user_Input < 0:
    print("Invalid input, you lose.")
else:

    user_Wep = (wep_Choice[user_Input])

# test line
# print(wep_Choice[wep_Random])

# conditions when user chooses rock
    if user_Input == 0:
        print(f"{user_Wep}\nComputer chose:\n{wep_Computer}")
        if wep_Random == 1:
            print("You lose")
        elif user_Input < wep_Random:
            print("You win")
        else:
            print("Tie!")

# conditions when user chooses paper
    elif user_Input == 1:
        print(f"{user_Wep}\nComputer chose:\n{wep_Computer}")
        if user_Input < wep_Random:
            print("You lose")
        elif user_Input > wep_Random:
            print("You win")
        else:
            print("Tie!")

# conditions when user chooses scissors
    else:
        print(f"{user_Wep}\nComputer chose:\n{wep_Computer}")
        if wep_Random == 0:
            print("You lose")
        elif user_Input > wep_Random:
            print("You win")
        else:
            print("Tie!")