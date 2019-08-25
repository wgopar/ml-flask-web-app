from flask import Flask, request, render_template, redirect, url_for
from utils import clean_text
import pickle
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    """ Main webpage with user input through form and prediction displayed

    :return: main webpage host, displays prediction if user submitted in text field
    """

    if request.method == 'POST':

        # prepare input text
        response = request.form['text']
        input_text = clean_text(response)

        # load vectorizer and transform input text
        vectorizer_path = os.path.join(os.getcwd(), 'model_assets', 'vectorizer_test_v.0.0.pkl')
        vectorizer = pickle.load(open(vectorizer_path, 'rb'))
        input_text = vectorizer.transform([input_text])

        # load model
        model_path = os.path.join(os.getcwd(), 'model_assets', 'model_test_v.0.0.pkl')
        model = pickle.load(open(model_path, 'rb'))

        # predict
        prediction = model.predict(input_text)
        prediction = 'Cyber-Troll' if prediction[0] == 1 else 'Non Cyber-Troll'

        return render_template('index.html', text=prediction, submission=response)

    if request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
