from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
from blueprints.answers import answers
from customhandlers.customresponse import CustomResponse

import os
import sys
import datetime
from importlib import reload

current_dir = os.getcwd()
server_dir = os.path.join(current_dir, "../../server")
uploads_dir = os.path.join(server_dir, 'uploads')
blueprint_dir = os.path.join(server_dir, 'blueprint')
sys.path.append(current_dir)
sys.path.append(uploads_dir)
sys.path.append(blueprint_dir)

app = Flask(__name__)
CORS(app)

#app.register_blueprint(answers)
app.response_class = CustomResponse
app.config['UPLOAD_FOLDER'] = 'uploads/'

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
db = myclient["youthcode"]

db_collection = db["answers"]

counter = 0
import json
import random
from bson.json_util import dumps

class AnswerList(Resource):

    def get(self):
        return dumps(db_collection.find({}))

    def post(self, file):
        filename_no_extension = file.filename.split(".")
        if file:
            full_file_path = os.path.join(uploads_dir, file.filename)
            with open(full_file_path, 'r') as f:
                content = f.read()
                file_name_counter_no_ex = filename_no_extension[0] + str(random.randint(1, 1000000))
                file_name_counter = file_name_counter_no_ex + ".py"
                new_file_full_path = os.path.join(uploads_dir, file_name_counter)
                with open(new_file_full_path, 'w') as fw:
                    fw.write(content)
                    print(content)
                    class_path = "uploads." + file_name_counter_no_ex
                    module = __import__(class_path)
                    module = getattr(module, file_name_counter_no_ex)
                    #result = module.foo()
                    result = exec(content)


                    item = db_collection.find({"groupId": result["groupId"]})
                    temp = list(item)
                    if len(list(item)) > 0:
                        print("if")
                        print(result)
                        temp["groupId"] = result["groupId"]
                        temp["receivedTime"] = datetime.datetime.today().strftime("%X")
                        temp["result"] = result["result"]
                        temp["questionNum"] = result["questionNum"]
                        db_collection.insert_one(temp)
                    else:
                        print("else")
                        print(result)
                        obj = dict()
                        obj["groupId"] = result["groupId"]
                        obj["receivedTime"] = datetime.datetime.today().strftime("%X")
                        obj["result"] = result["result"]
                        obj["questionNum"] = result["questionNum"]
                        db_collection.insert_one(obj)

                    if result['result'] == 5:
                        response = {"message": "Correct answer!"}
                    else:
                        response = {"message": "Incorrect answer!"}
                    return response


@app.route('/api/answer', methods=['GET', 'POST'])
def handleRequest():
    if request.method == "POST":
        return AnswerList().post(request.files['file'])
    else:
        return AnswerList().get()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=False)
