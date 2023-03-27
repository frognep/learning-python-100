print("Welcome to the rollercoaster!")
user_Height = int(input("What is your height in cm? "))
user_Age = int(input("What is your age? "))

if user_Height > 120:  # if condition is not met, nested condition(s) are skipped
    print("You are allowed to go on the rollercoaster!")
    if user_Age < 12:
        print("You pay $5.")
    elif user_Age <= 18:
        print("You pay $7")
    elif user_Age >= 45 and user_Age <= 55:
        print("Your ticket is free.")
    else:
        print("You pay $12.")
else:
    print("I'm sorry, you do not meet the height requirement.")