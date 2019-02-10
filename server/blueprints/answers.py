from flask import Blueprint, request
import json
import os
import sys
current_dir = os.getcwd()
uploads_dir = os.path.join(current_dir, 'uploads')
sys.path.append(current_dir)
sys.path.append(uploads_dir)

answers = Blueprint('answers', __name__)


def import_answer_class(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


@answers.route('/api/answer', methods=('GET', 'POST'))
def handle_answers():
    if request.method == "POST":
        response = {}
        file = request.files['file']
        filename_no_extension = file.filename.split(".")
        if file:
            full_file_path = os.path.join(uploads_dir, file.filename)
            file.save(full_file_path)
            class_path = "uploads." + filename_no_extension[0]
            module = import_answer_class(class_path)
            result = module.foo()
            if result['result'] == 5:
                response = {"message": "Correct answer!"}
            else:
                response = {"message": "Incorrect answer!"}
            return response
    else:
        return {"message":"Hello World"}
