student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
  stored_score =  student_scores[student]
  if stored_score >= 91:
    stored_score = "Outstanding"
  elif stored_score >= 81:
    stored_score = "Exceeds Expectations"
  elif stored_score >= 71:
    stored_score = "Acceptable"
  else: 
    stored_score = "Fail"
  student_grades[student] = stored_score
  
# 🚨 Don't change the code below 👇
print(student_grades)