from os import system
from clear_function import clear
import pandas as pd

clear()


data = pd.read_csv("squirrel\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(data)

gray_fur = data[data.Primary_Fur_Color == "Gray"]
red_fur = data[data.Primary_Fur_Color == "Cinnamon"]
black_fur = data[data.Primary_Fur_Color == "Black"]

# print(gray_fur)

gray_count = len(gray_fur)
red_count = len(red_fur)
black_count = len(black_fur)

squirrel_color = {
    "color": ["gray", "red", "black"],
    "count": [gray_count, red_count, black_count]
}

dict_to_dataframe = pd.DataFrame(squirrel_color)

# print(dict_to_dataframe)

dict_to_dataframe.to_csv("squirrel\\squirrel_fur_count.csv")


# print(len(gray_fur))
# print('\n')

# print(len(red_fur))
# print('\n')

# print(len(black_fur))
# print('\n')

