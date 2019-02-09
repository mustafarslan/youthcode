from flask import Blueprint, request

answers = Blueprint('answers', __name__)

@answers.route('/api/answer', methods=('GET', 'POST'))
def handleAnswers():
    if request.method == "POST":
        pass
    else:
        return {"message":"Hello World"}
