from flask import Flask, request, render_template, jsonify, url_for
from utils import clean_text
import pickle
import time
import os

app = Flask(__name__)

MODEL_VERSION = 'model_V0.pkl'
VECTORIZER_VERSION = 'vectorizer_V0.pkl'

# load model assets
vectorizer_path = os.path.join(os.getcwd(), 'model_assets', VECTORIZER_VERSION)
model_path = os.path.join(os.getcwd(), 'model_assets', MODEL_VERSION)
vectorizer = pickle.load(open(vectorizer_path, 'rb'))
model = pickle.load(open(model_path, 'rb'))

# TODO: add versioning to url
@app.route('/', methods=['GET', 'POST'])
def predict():
    """ Main webpage with user input through form and prediction displayed

    :return: main webpage host, displays prediction if user submitted in text field
    """

    if request.method == 'POST':

        response = request.form['text']
        input_text = clean_text(response)
        input_text = vectorizer.transform([input_text])
        prediction = model.predict(input_text)
        prediction = 'Cyber-Troll' if prediction[0] == 1 else 'Non Cyber-Troll'
        return render_template('index.html', text=prediction, submission=response)

    if request.method == 'GET':
        return render_template('index.html')

# TODO: add versioning to api
@app.route('/predict', methods=['POST'])
def predict_api():
    """ endpoint for model queries (non gui)

    :return: json, model prediction and response time
    """
    start_time = time.time()

    request_data = request.json
    input_text = request_data['data']
    input_text = clean_text(input_text)
    input_text = vectorizer.transform([input_text])
    prediction = model.predict(input_text)
    prediction = 'Cyber-Troll' if prediction[0] == 1 else "Non Cyber-Troll"  # post processing

    response = {'prediction': prediction, 'response_time': time.time() - start_time}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
