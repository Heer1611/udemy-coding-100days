from typing import Self
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank =[]
for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]
    new_question = Question(question_text, question_ans)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)
while quiz.Still_has_q():
    quiz.next_q()
    
print("You've  completed the quiz")
print(f"your final score was {quiz.user_score}/{quiz.question_num}")