from function import clear
import pandas as pd

clear()

NATO_df = pd.read_csv("day26_LIST_DICT_COMPREHENSION/NATO-alphabet-start/nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter:row.code for (index, row) in NATO_df.iterrows()}

# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your name: ")
# user_input = "danny"

# outlining logic
# for letter in user_input:
#     result_dict = [code_dict for (letter_dict, code_dict) in nato_dict.items() if letter_dict == letter.upper()]
#     for (letter_dict, code) in nato_dict.items():
#         if letter_dict == letter.upper():
#             print(code)

# for item in nato_dict.items():
#     print(item)

# my solution
result_dict = [code for letter_user in user_input for (letter, code) in nato_dict.items() if letter == letter_user.upper()]

# Dr. Angela's solution
# Thoughts: Very clever and clean. The thought of using a dictionary key to call the value slipped my mind.
# result_dict = [nato_dict[f"{letter.upper()}"] for letter in user_input]

print(result_dict)