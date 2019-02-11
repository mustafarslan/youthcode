from flask import Blueprint

class AnswerBlueprint(Blueprint):

    answerList = []

    def set_answers(self, data):
        # here you can make extra task like ensuring if
        # a minum group of value were provided for instance
        answerList = data

    def get_answers(self):
        return self.answerList
