# Allow the player to submit a guess for a number between 1 and 100. >>DONE<<
# Check user's guess against actual answer. Print "Too high." or "Too low." 
# depending on the user's answer. >>DONE<<
# If they got the answer correct, show the actual answer to the player. >>DONE<<
# Track the number of turns remaining. >>DONE<<
# If they run out of turns, provide feedback to the player. >>DONE<<

import os
import random
from art import logo

def clear():
    os.system('cls')

def easy_level():
    global user_attempts

    user_attempts = 10

    return user_attempts

def hard_level():
    global user_attempts

    user_attempts = 5

    return user_attempts

# ---------------------------- #
# MAIN

# GLOBAL_VARIABLE
USER_ATTEMPTS = 0


user_attempts = 0
clear()
print(logo)
print("Welcome to the Number Guessing Game!\n"
    "I'm thinking of a number between 1 and 100.")
user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if user_difficulty == 'easy':
    easy_level()
else:
    hard_level()

guess_answer = random.choice(range(1,101))
# print(guess_answer)

game_over = False
while (game_over != True and user_attempts > 0):
    user_guess = int(input("Guess the number: "))

    if user_attempts > 0:
        if user_guess > guess_answer:
            print("too high!\n")
        elif user_guess < guess_answer:
            print("too low!\n")
        elif user_guess == guess_answer:
            game_over = True
        else:
            print("idk")
        user_attempts -= 1
        print(f"Lives left: {user_attempts}")
    else:
        game_over = True

print(f"Lives left: {user_attempts}")
print("You lose. No more turns.")

if user_attempts == 0:
    clear()
    print(logo)
    print("\nYou lose. No more turns.")
else:
    clear()
    print(logo)
    print(f"\nYou win! {guess_answer} was the number! :]")

