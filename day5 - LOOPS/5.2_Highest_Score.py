# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# initiate two accumulators
# original_Score holds the score being compared to the new score
# highest_Score will be updated only if the compared score is greater
# original_Score = 0
highest_Score = 0
for score in student_scores:
  # if score < high_Score, if-statement is false and loop continues to evaluate next number in list
  if score > highest_Score:
    highest_Score = score

print(f"The highest score in the class is {highest_Score}")


