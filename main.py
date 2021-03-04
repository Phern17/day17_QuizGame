from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item['question'], item['correct_answer']))


quiz_control = QuizBrain(question_bank)

while quiz_control.still_has_question():
    quiz_control.next_question()

print(f"You've completed the quiz!\nYour final score is {quiz_control.score}/{quiz_control.question_number}")
