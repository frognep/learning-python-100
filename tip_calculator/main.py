# 09/05/22
print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill?: $"))
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15?: "))
num_of_people = int(input("How many people to split the bill?: "))

tip_calculation = total_bill * (percent_tip / 100)

total_w_tip = total_bill + tip_calculation
total_for_all = total_w_tip / num_of_people

print(f"Each person should pay: ${total_for_all:.2f}") #-string to format final amount to the nearest 2 decimal places