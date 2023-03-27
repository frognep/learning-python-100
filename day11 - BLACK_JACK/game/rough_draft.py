# TO DO ##
# write compare function to compare scores and output win/loss/draw statements
from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clear():
    os.system("clear")

def calculate_score(list):
    calculation = 0
    for card in list:
        calculation += card
    if 11 in list and 10 in list and len(list) == 2:
        return 0
    elif 11 in list and calculation > 21:
        list.remove(11)
        list.append(1)
        new_calc = calculate_score(list)
        return new_calc
    elif calculation == 21:
        return 0
    elif calculation > 21:
        return calculation
    else:
        return calculation

def compare_scores(user_score, computer_score):
    if user_score == computer_score:
        print("Draw!\n")
    # ------------------------------- #
    # Black Jack conditions
    elif user_score == 0:
        print("Black Jack! You win.\n")
    elif computer_score == 0:
        print("You lose.\n")
    # ------------------------------- #
    # Bust conditions
    elif user_score > 21:
        print("Bust! You lose.\n")
    elif computer_score > 21:
        print("You win!\n")
    # ------------------------------- #
    # Non- Black Jack win conditions
    elif computer_score > user_score:
        print("You lose! ):\n")
    else:
        print("You win! :D\n")
    


def deal_card():
    user_cards = []
    computer_cards = []
    # deals the >first< two cards to the USER
    user_score = calculate_score(user_cards)
    
    if len(user_cards) == 0:
        for card in range(2):
            random_card_pull = random.choice(cards)
            user_cards.append(random_card_pull)

        # deals the >first< single card to the COMPUTER
        user_score = calculate_score(user_cards)

        print(f"\tYour cards: {user_cards}, current score: {user_score}")
        computer_cards.append(random.choice(cards))

    # deals one additional card to user's deck
    elif len(user_cards) > 1 and user_score < 21:
        user_cards.append(random.choice(cards))
        user_score = calculate_score(user_cards)

        print(f"\n\tYour cards: {user_cards}, current score: {user_score}")

    print(f"\tComputer's first card: {computer_cards[0]}")

    # ------------------------------------------------------------------ #
    # win/bust & add conditions, 0 == 21
    computer_score = calculate_score(computer_cards)
    
    if user_score == 0 or computer_score == 0:
        compare_scores(user_score, computer_score)

    # if user has not reached 21, option to add card or not
    elif user_score < 21:
        add_card = input("Enter 'y' to add card, Enter 'n' to quit: ").lower()

        # if yes, deals next card
        if add_card == 'y':
            user_deal = deal_card()

        # if no, computer draws cards while score < 17
        elif add_card == 'n':
            while not computer_score > 17:
                computer_cards.append(random.choice(cards))
                computer_score = calculate_score(computer_cards)
            print(f"\n\tYour final hand: {user_cards}, final score: {user_score}\n"
                  f"\tComputer's final hand: {computer_cards}, final score: {computer_score}\n")
            compare_scores(user_score, computer_score)
    else:
        print(f"\tYour final hand: {user_cards}, final score: {user_score}\n"
                  f"\tComputer's final hand: {computer_cards}, final score: {computer_score}\n")
        compare_scores(user_score, computer_score)

clear()
print(logo)
deal_card()
        
# -------------------------- #
# MAIN -- FIX

# play_game = input("Would you like to play a game of Blackjack? Enter 'y' or 'n': ").lower()

# if play_game == 'y':
#     clear()
#     print(logo)
#     deal_card()
#     play_again_bool = True
#     while play_again_bool == True:
#         play_again = input("Would you like to play again? Enter 'y' or 'n': ").lower()
#         if play_again == 'y':
#             clear()
#             print(logo)
#             new_game_start = deal_card()
#         else:
#             play_again_bool = False
# print("Thank you for checking out my variation of Blackjack! :]\n")
    

# switch = True
# while switch == True:
#     print(logo)
#     user_start_deal = deal_card()
#     play_again = input("Enter 'y' to play again. Enter 'n' to quit: ").lower()
#     while play_again == "y":
#         clear()
#         print(logo)
#         new_deal = deal_card()
#     else:
#         switch = False
#         clear()