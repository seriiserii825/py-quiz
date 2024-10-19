import requests
import html
from Question import Question
from QuizBrain import QuizBrain
# from data import question_data

url = 'https://opentdb.com/api.php?amount=10&type=boolean'

questions = requests.get(url).json()['results']
question_data = []
for item in questions:
    try:
        question_data.append({
            "text": html.unescape(item['question']),
            "answer": html.unescape(item['correct_answer'])
            })
    except KeyError:
        print(f'KeyError: {item}')

question_bank = []
for item in question_data:
    question = Question(item['text'], item['answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.stillHasQuestions():
    quiz.nextQuestion()

quiz.finalScore()
