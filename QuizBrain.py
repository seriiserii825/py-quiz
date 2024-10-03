class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def stillHasQuestions(self):
        return self.question_number < len(self.question_list)

    def nextQuestion(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number}: {current_question.text} (True,False)?")
        return response
