from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html

question_bank = []

for question in question_data:
    question_text = html.unescape(question["question"])
    question_ans = question["correct_answer"]
    new_question = Question(question_text, question_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("Congrats !! You have completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")