from flask import Blueprint, request
from .AnswerBlueprint import AnswerBlueprint
from importlib import reload
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


answers = AnswerBlueprint('answers', __name__)



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
            module = reload(__import__(class_path))
            module = getattr(reload(module), filename_no_extension[0])
            result = module.foo()
            print("result ")
            print(result)
            #os.remove(full_file_path)

            answers_list = answers.get_answers()
            print(answers_list)
            if not any(item["groupId"] == result["groupId"] for item in answers_list):
                result["receivedTime"] = datetime.datetime.today().strftime("%X")
                answers_list.append(result)
                answers.set_answers(answers_list)
                print(answers_list)
            else:
                print("in else")
                for item in answers_list:
                    if result["groupId"] == item["groupId"]:
                        consist = True
                        answers_list.remove(item)
                        print("in for if")
                        result["receivedTime"] = datetime.datetime.today().strftime("%X")
                        answers_list.append(result)
                        answers.set_answers(answers_list)
                print(answers_list)
            if result['result'] == 5:
                response = {"message": "Correct answer!"}
            else:
                response = {"message": "Incorrect answer!"}
            return response
    else:
        return answers.get_answers()
