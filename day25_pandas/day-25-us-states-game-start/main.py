from function import clear
import string
import turtle
import pandas as pd
clear()

# -----------------------
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "day-25-us-states-game-start\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.up()
pen.hideturtle()

# -----------------------
states_file = pd.read_csv("day-25-us-states-game-start\\50_states.csv")
state_list = states_file["state"].to_list()

# alternative:
# state_data = data[data.state == answer_state]
# int(state_data.x) to pull x, int(state_data.y) to pull y

# -----------------------
states_correctly_guessed = []
user_answer = ""
while len(states_correctly_guessed) != 50:
    if len(states_correctly_guessed) == 0:
        user_input = screen.textinput(title="Guess the State", prompt="Enter a State: ")
    else:
        user_input = screen.textinput(title=f"{len(states_correctly_guessed)}/50 States Correct", prompt="Enter a State: ")

    if user_input.lower() == "exit":
        states_not_guessed = []
        for item in state_list:
            if item not in states_correctly_guessed:
                states_not_guessed.append(item)

        # utilizing g4g on knowledge on converting list to a dataframe for csv conversion
        df = pd.DataFrame(states_not_guessed)
        df.to_csv("day-25-us-states-game-start\\incorrect.csv")
        break

    user_answer = string.capwords(user_input)
    if user_answer in state_list and user_answer not in states_correctly_guessed:
        states_correctly_guessed.append(user_answer)
        state = states_file[states_file.state == user_answer]
        pen.goto(int(state.x.iloc[0]), int(state.y.iloc[0]))
        pen.write(f"{user_answer}")

# -----------------------
        


