

# obtains user's body input
#inputs, 1.8 & 89 = 27
user_Height = 1.5 #float(input("Enter your height in m: "))
user_Weight = 51 #float(input("Enter your weight in kg: "))


BMI_Calc = round(user_Weight // user_Height ** 2)

print(f"Your BMI is {BMI_Calc}, ", end = "")

if BMI_Calc < 18.5:
    print("you are underweight.")
elif BMI_Calc <= 25:
    print("you are normal weight.")
elif BMI_Calc <= 30:
    print("you are slightly overweight.")
elif BMI_Calc <= 35:
    print("you are obese.")
else:
    print("you are clinically obese.")
