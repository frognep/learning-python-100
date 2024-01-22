import random

## list-comprehension
# numbers = [1, 2, 3]
# new_list = [n+1 for n in numbers]
# print(new_list)

# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# new_list = [name.upper() for name in names if len(name) > 4]
# print(new_list)

## dict-comprehension

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
student_score = {student:random.randint(1,100) for student in names}

print(student_score)

passed_students = {student:"passed" for (student, score) in student_score.items() if score > 70}

print(passed_students)