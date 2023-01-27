from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clear():
    os.system('clear')

def calculate_score(deck):
    score = 0
    for card in deck:
        score += card

    # black-jack
    if score == 21:
        return 0
    
    elif score > 21:
        return score
    
    # 11 + 10 = 21 ## black-jack!
    elif 11 in deck and 10 in deck and len(deck):
        return 0

    # ace 11 or 1
    elif 11 in deck and score > 21:
        deck.remove(11)
        deck.append(1)
    
    else:
        return score


def compare_scores(user_score, computer_score):
    if user_score == computer_score:
        print("Draw\n")
    
    # one-side win conditions
    elif user_score == 0:
        print("Black Jack!\n")
    
    elif computer_score == 0:
        print("You lose.\n")

    # user win-lose conditions
    elif user_score > 21:
        print("Bust! You lose.\n")

    elif computer_score > 21:
        print("You win!\n")

    elif user_score > computer_score:
        print("You win!\n")
    
    elif computer_score > user_score:
        print("You lose!\n")

# stores the cards given/added to the players
user_deck = []
computer_deck = []
def main_draw():
    
    user_score = calculate_score(user_deck)
    computer_score = calculate_score(computer_deck)

    # deal first card(s) to player and computer
    if len(user_deck) == 0 and len(computer_deck) == 0:
        for give_user in range(2):
            user_deck.append(random.choice(cards))
        computer_deck.append(random.choice(cards))
        print(f"\tYour cards: {user_deck}, score: {calculate_score(user_deck)}")
        print(f"\tComputer's first card: {computer_deck[0]}")
        user_score = calculate_score(user_deck)
        computer_score = calculate_score(computer_deck)

# ------------------------------------------------------------------ #
    # if 21 has not been reached, another card will be added
    elif len(user_deck) > 1 and user_score < 21:
        user_deck.append(random.choice(cards))
        user_score = calculate_score(user_deck)
        
        print(f"\tYour cards: {user_deck}, current score: {user_score}\n"
              f"\tComputer's first card: {computer_deck[0]}")
    
    # if over 21, user loses and final results are outputted
    elif len(user_deck) > 2 and user_score > 21:
        print(f"\tYour final hand: {user_deck}, final score: {user_score}\n"
                    f"\tComputer's final hand: {computer_deck}, final score: {computer_score}\n")
        compare_scores(user_score, computer_score)

# ------------------------------------------------------------------ #
    user_score = calculate_score(user_deck) 

    # draw condition
    if user_score == 0 or computer_score == 0:
        compare_scores(user_score, computer_score)
    
    # user score is less than 21
    elif user_score < 21:
        add_card = input("Would you like to add a card? Enter 'y' or 'n': ").lower()

        # draw another card
        if add_card == 'y':
            main_draw()

        # end turn and let computer draw as long as score is less than 17    
        elif add_card == 'n':
            switch = False
            while switch == False:
                if computer_score < 17:
                    computer_deck.append(random.choice(cards))
                    computer_score = calculate_score(computer_deck)
                else:
                    switch = True
            print(f"\tYour final hand: {user_deck}, final score: {user_score}\n"
                  f"\tComputer's final hand: {computer_deck}, final score: {computer_score}\n")
            compare_scores(user_score, computer_score)

    else:
        print(f"\tYour final hand: {user_deck}, final score: {user_score}\n"
                  f"\tComputer's final hand: {computer_deck}, final score: {computer_score}\n")
        compare_scores(user_score, computer_score)

# ------------------------------------------------------------------ #
#MAIN
clear()
user_play = input("Would you like to play blackjack? Enter 'y' or 'n': ").lower()
if user_play == 'y':
    clear()
    print(logo)
    main_draw()
    switch = False
    while switch != True:
        user_play_again = input("\nWould you like to play again? Enter 'y' or 'n': ")
        if user_play_again == 'y':
            clear()
            user_deck = []
            computer_deck = []
            main_draw()
        else:
            switch = True

clear()
print('\nThank you for checking out my variation of Blackjack! :]\n')
