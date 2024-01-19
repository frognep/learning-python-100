from os import system
from clear_function import clear
import pandas as pd

clear()

data = pd.read_csv("weather\\weather_data.csv")

# print(data["day"][0])
# print(type(data["temp"]))

# converting data frames
# ------------------
# data_dict = data.to_dict()

# data_temp_list = data["temp"].to_list()
# print(data_temp_list)

# ------------------
# series functions
# avg_weekly_temp = sum(data_temp_list) / len(data_temp_list)
# print(avg_weekly_temp)

# print(data["temp"].mean())
# print(data["temp"].max())

# ------------------
# pulling out data from a row
# print(data[data.day == "Monday"])

# print(data[data.temp == data["temp"].max(0)])

# monday = data[data.day == "Monday"]

# print(monday.temp)

# c_to_f = ((monday.temp) * 1.8) + 32

# print(c_to_f)

# creating a dataframe from scratch

# converting dictionary to dataframe, and dataframe to .csv

# ------------------
# exercise 2
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# dict_to_dataframe = pd.DataFrame(data_dict)

# # print(dict_to_dataframe)

# dict_to_dataframe.to_csv("weather\\new_data.csv")