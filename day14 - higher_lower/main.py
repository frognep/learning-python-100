from os import system
import art
import sheet
import random

# game: compare follower amounts between Instagram influencers
# game ends: continues until user answers wrong

# flow --
# 50 individuals in data-sheet
# if user is correct, score is added, if incorrect game ends
# challenge: incoporate main game into a function

def clear():
    system("cls")

def add_to_user_score():
    return user_score + 1

def play_game():
    instagram_user1 = sheet.data[random.randint(1, (50 - 1))]
    instagram_user2 = sheet.data[random.randint(1, (50 - 1))]
    print(art.logo)
    if user_score > 0:
        print(f"You're right! Current score: {user_score}")
    print(f"Compare A: {instagram_user1['name']}, a {instagram_user1['description']}, from {instagram_user1['country']}.")
    print(art.vs)
    print(f"Against B: {instagram_user2['name']}, a {instagram_user2['description']}, from {instagram_user2['country']}.")
    user_answer = input("Who has more followers? Enter 'A' or 'B': ").upper()
        
    if user_answer == 'A':
        if instagram_user1['follower_count'] > instagram_user2['follower_count']:
            return 1
        else:
            return 0   
    else:
        if instagram_user1['follower_count'] < instagram_user2['follower_count']:
            return 1
        else:
            return 0

user_score = 0
start_game = play_game()

user_alive = True
while user_alive:
    if start_game == 1:
        user_score = add_to_user_score()
        # print(user_score)
        clear()
        start_game = play_game()
    else:
        clear()
        print(art.logo)
        print(f"Sorry that's wrong. Final score: {user_score}")
        user_alive = False

print("Game Over.")

# FINISHED: 02/21 2:44PM CST
# [[WHAT I LEARNED]]:
# How to separate code into clean individual blocks instead of implementing everything into one clustered function
# Improved on global/local scope variable differentiation

# ============================================================================

# issues for next time:: [[SOLVED]]
# - where to put user_score variable
# - implement score-keeping function possibly?

# solution:
# create a separate function to add to the user's score