from flask import Flask
from flask_cors import CORS
from blueprints.answers import answers
from customhandlers.customresponse import CustomResponse

app = Flask(__name__)
CORS(app)

app.register_blueprint(answers)
app.response_class = CustomResponse
app.config['UPLOAD_FOLDER'] = 'uploads/'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=False)
