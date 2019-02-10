from flask import Flask
from blueprints.answers import answers
from customhandlers.customresponse import CustomResponse

app = Flask(__name__)

app.register_blueprint(answers)
app.response_class = CustomResponse
app.config['UPLOAD_FOLDER'] = 'uploads/'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=False)
