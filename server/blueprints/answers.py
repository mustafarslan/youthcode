from flask import Blueprint, request

answers = Blueprint('answers',__name__)

@answers.route('/answer', methods=('GET', 'POST'))
def handleAnswers():
    if request.method == "POST":
        pass
    else:
        return {"message":"Hello World"}
