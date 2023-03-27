############DEBUGGING#####################

# clear function
from os import system
def clear():
    system("cls")

clear()

# Describe Problem: range(start, stop), stop immediately ends once i = 20
# so we must +1 to the end of the range
def my_function():
  for i in range(1, (20 + 1)):
    if i == 20:
        print("You got it")
# my_function()

# Reproduce the Bug
# Bug: IndexError: list index out of range
# Hypothesis 1: end of randint's range is out of list bounds.
# List index starts from 0, range starts from actual end-points
# Solution, we change the randint range to (0, 5)
def roll_dice():
    from random import randint
    dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
    dice_num = randint(0, (6 - 1))
    print(dice_imgs[dice_num])
    # print(len(dice_imgs))
    # print(dice_imgs[5])
# roll_dice()

# # Play Computer
# year = int(input("What's your year of birth?: "))
# if year >= 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?: "))
# if age > 18:
#     print(f"You can drive at age {age}.")

# # #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# # print(pages)
# # print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])