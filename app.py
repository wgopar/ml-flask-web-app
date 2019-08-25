from flask import Flask, request, render_template, redirect, url_for
from utils import clean_text
import pickle
import os

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predict():

    response = request.json

    # load vectorizer
    vectorizer_path = os.path.join(os.getcwd(), 'model_assets', 'vectorizer_test_v.0.0.pkl')
    vectorizer = pickle.load(open(vectorizer_path, 'rb'))

    # clean input text and transform
    filtered_text = clean_text(response['data'])
    input_text = vectorizer.transform([filtered_text])

    # load model
    model_path = os.path.join(os.getcwd(), 'model_assets', 'model_test_v.0.0.pkl')
    model = pickle.load(open(model_path, 'rb'))

    # predict
    prediction = model.predict(input_text)
    prediction = 'Cyber-Troll' if prediction[0] == 1 else 'Non Cyber-Troll'

    return render_template('index.html', text=prediction)


if __name__ == '__main__':
    app.run(debug=True)
