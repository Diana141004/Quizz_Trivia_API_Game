from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for index in range(12):
        ans_object = Question(question_data["results"][index]["question"],question_data["results"][index]["correct_answer"])
        question_bank.append(ans_object)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!!")
print(f"You're final score is {quiz.score}/{quiz.question_number}")