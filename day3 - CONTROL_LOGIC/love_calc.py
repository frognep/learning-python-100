# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# combined both names into one lower cased string
combined_name = name1.lower() + name2.lower()

# counts amount of each individual letter from the word 'true' in both names
num_t = combined_name.count("t")
num_r = combined_name.count("r")
num_u = combined_name.count("u")
num_e = combined_name.count("e")

# counts amount of each individual letter from the word 'love' in both names
num_l =  combined_name.count("l")
num_o =  combined_name.count("o")
num_v =  combined_name.count("v")
num_e2 = num_e

# sum of letters 'true' in both names
sum_of_true = num_t + num_r + num_u + num_e

# sum of letters 'love' in both names
sum_of_love = num_l + num_o + num_v + num_e2

# true love computations, combine both individual numbers into one real number
sum_of_true_love = int(str(sum_of_true) + str(sum_of_love))

# conditions and statements using and/or and f-strings
if (sum_of_true_love < 10) or (sum_of_true_love > 90):
    print(f"Your score is {sum_of_true_love}, you go together like coke and mentos.")
elif (sum_of_true_love >= 40) and (sum_of_true_love <= 50):
    print(f"Your score is {sum_of_true_love}, you are alright together.")
else:
    print(f"Your score is {sum_of_true_love}.")