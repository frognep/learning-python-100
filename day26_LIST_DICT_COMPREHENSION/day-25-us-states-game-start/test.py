from weather.clear_function import clear
import string
import turtle
import pandas as pd
import string

clear()
states_data = pd.read_csv("G:\\code\\udemy\\day25_pandas\\day-25-us-states-game-start\\50_states.csv")



state_list = states_data["state"].to_list()

# print(state_list)

# if string.capwords("new york") in state_list:
#     print("true")
# else:
#     print('false')

states_correctly_guessed = [""]

states_not_guessed = []
for item in state_list:
    if item not in states_correctly_guessed:
        states_not_guessed.append(item)

print(states_not_guessed)
