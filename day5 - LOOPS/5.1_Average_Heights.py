# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# cannot use len() or sum()
# use for loop to calculate how many items are in the list

# we set total_Num to 0 to initiate an accumulator
total_Num = 0
for student in student_heights:
  total_Num += 1

# use for loop to calculate the sum of all numbers in the list
sum_Of_Student_Heights = 0
for height in student_heights:
  sum_Of_Student_Heights += height

average_Height = round(sum_Of_Student_Heights / total_Num)

print(average_Height)