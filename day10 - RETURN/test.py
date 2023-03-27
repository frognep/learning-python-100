def add(num1, num2):
    return num1 + num2


colors = {
    "+": add,
    "2": "Green",
    "3": "Blue"
}

print(colors["+"](2,2))