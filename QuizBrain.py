class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def stillHasQuestions(self):
        return self.question_number < len(self.question_list)

    def nextQuestion(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number}: {current_question.text} (True,False)?")
        self.checkAnswer(response, current_question.answer)

    def checkAnswer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You got it')
            self.score += 1
        else:
            print('Thats wrong')
        print(f"The correct answer: {correct_answer}")
        print(f"Your current score: {self.score}/{self.question_number}")
        print("\n")

    def finalScore(self):
        print("You've completed the quiz")
        print(f"Your final score: {self.score}/{self.question_number}")
