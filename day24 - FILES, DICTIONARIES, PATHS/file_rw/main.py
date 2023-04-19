from os import system

def clear():
    system("cls")

clear()

last_score = 10
with open(r"F:\code\udemy\day24\file_rw\data.txt", mode="r") as highscore_file:
    content = highscore_file.read()
    print(content)