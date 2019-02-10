from flask import Blueprint, request
import json
import os
import sys
import datetime
import time

current_dir = os.getcwd()
server_dir = os.path.join(current_dir, "../../server")
uploads_dir = os.path.join(server_dir, 'uploads')
blueprint_dir = os.path.join(server_dir, 'blueprint')
sys.path.append(current_dir)
sys.path.append(uploads_dir)
sys.path.append(blueprint_dir)


answers = Blueprint('answers', __name__)

answerList = []


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
            os.remove(full_file_path)

            consist = False

            for item in answerList:
                if result["groupId"] == item["groupId"]:
                    consist = True
                    item["questionNum"] = result["questionNum"]
                    item["receivedTime"] = datetime.datetime.today().strftime("%X")
                    item["result"] = result["result"]
            else:
                obj = {}
                obj["groupId"] = result["groupId"]
                obj["questionNum"] = result["questionNum"]
                obj["receivedTime"] = datetime.datetime.today().strftime("%X")
                obj["result"] = result["result"]
                print(obj)
                answerList.append(obj)

            if result['result'] == 5:
                response = {"message": "Correct answer!"}
            else:
                response = {"message": "Incorrect answer!"}
            return response
    else:
        return answerList
