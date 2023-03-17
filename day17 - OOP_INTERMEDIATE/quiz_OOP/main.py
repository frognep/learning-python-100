from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
from os import system

def clear():
    system("cls")

clear()

# creating the question_bank via for-loop
question_bank = []
for item in range(len(question_data)):
    extract_question = question_data[item]["question"]
    extract_answer   = question_data[item]["correct_answer"]
    new_question     = Question(text=extract_question, answer=extract_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!\n")
print(f"Your final score is {quiz.score}/{len(question_data)}")