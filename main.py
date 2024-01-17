from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range(len(question_data)):
    q_text = question_data[i]["question"]
    q_answer = question_data[i]["correct_answer"]
    question_bank.append(Question(q_text, q_answer))

quiz = QuizBrain(question_bank)
quiz.next_question()


while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")