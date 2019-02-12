from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
from customhandlers.customresponse import CustomResponse

import os
import sys
import datetime
import pymongo
import json
from bson.json_util import dumps

current_dir = os.getcwd()
server_dir = os.path.join(current_dir, "../../server")
uploads_dir = os.path.join(server_dir, 'uploads')
blueprint_dir = os.path.join(server_dir, 'blueprint')
sys.path.append(current_dir)
sys.path.append(uploads_dir)
sys.path.append(blueprint_dir)

app = Flask(__name__)
CORS(app)

app.response_class = CustomResponse


myclient = pymongo.MongoClient("mongodb://localhost:27017")
db = myclient["youthcode"]

db_collection = db["answers"]


class AnswerList(Resource):

    def get(self):
        return dumps(db_collection.find({}))

    def post(self, data):
        json_data = json.loads(data.decode('utf8').replace("'", '"'))
        item = db_collection.find({"groupId": json_data["groupId"]})
        temp = list(item)
        print(temp)
        if len(temp) > 0:
            print("in if")
            db_collection.delete_many({"groupId": json_data["groupId"]})
            obj = dict()
            obj["groupId"] = json_data["groupId"]
            obj["receivedTime"] = datetime.datetime.today().strftime("%X")
            obj["result"] = json_data["result"]
            obj["questionNum"] = json_data["questionNum"]
            db_collection.insert_one(obj)
        else:
            obj = dict()
            obj["groupId"] = json_data["groupId"]
            obj["receivedTime"] = datetime.datetime.today().strftime("%X")
            obj["result"] = json_data["result"]
            obj["questionNum"] = json_data["questionNum"]
            db_collection.insert_one(obj)

        if json_data['result'] == 5:
            response = {"message": "Correct answer!"}
        else:
            response = {"message": "Incorrect answer!"}
        return response


@app.route('/api/answer', methods=['GET', 'POST'])
def handleRequest():
    if request.method == "POST":
        return AnswerList().post(request.data)
    else:
        return AnswerList().get()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=False)
