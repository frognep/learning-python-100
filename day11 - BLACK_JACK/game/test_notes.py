# -------------- TEST NOTES -------------- #

#             computer_score = calculate_score(computer_cards)
#             if computer_score < 17:
#                 computer_cards.append(random.choice(cards))
#                 # print(f"Your cards: {user_cards}\n"
#                 #         f"Computer cards: {computer_cards}")
#             else:
#                 switch = True
#                 print(f"Your final hand: {user_cards}, final score: {user_score}\n"
#                         f"Computer's final hand: {computer_cards}, final score: {computer_score}")

# elif add_card == 'n': 
#     switch = False
#     while switch != True:
#         computer_score = calculate_score(computer_cards)
#         if computer_score < 17:
#             computer_cards.append(random.choice(cards))
#             computer_score = calculate_score(computer_score)
#         else:
#             switch = True
#     print(computer_cards)

# def deal_comp_card():
#     computer_cards.append(random.choice(cards))
#     computer_score = calculate_score(computer_cards)

# print(user_cards)
# user_cards.append(random_card_pull)
# print(user_cards)

# return user_score

# test lists
# black_jack_list = [11, 10]
# print(calculate_score(black_jack_list))

# test_list = [11, 4]
# print(calculate_score(test_list))

# -------------- TEST NOTES -------------- #
# ---------------------------------------- #
# MAIN -- BROKEN

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

# ---------------------------------------- #