from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range(len(question_data)):
    q_text = question_data[i]["text"]
    q_answer = question_data[i]["answer"]
    question_bank.append(Question(q_text, q_answer))

quiz = QuizBrain(question_bank)
quiz.next_question()
