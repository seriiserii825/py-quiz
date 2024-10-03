from Question import Question
from QuizBrain import QuizBrain
from data import question_data

question_bank = []
for item in question_data:
    question = Question(item['text'], item['answer'])
    question_bank.append(question)
    
quiz = QuizBrain(question_bank)

while quiz.stillHasQuestions():
    quiz.nextQuestion()
