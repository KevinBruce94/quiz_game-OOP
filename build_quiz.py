from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

score = 0

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while QuizBrain.still_has_questions:
    quiz.next_question()


print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")




