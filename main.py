from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    one_question = Question(item["question"], item["correct_answer"])
    question_bank.append(one_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've finaly completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")
