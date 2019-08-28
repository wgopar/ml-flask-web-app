# ml-flask-web-app 

This is a simple flask application that acts as an Internet Cyber Troll Detector. Using the
Dataset for Detection of Cyber-Trolls ([here](https://dataturks.com/projects/abhishek.narayanan/Dataset%20for%20Detection%20of%20Cyber-Trolls/))
a binary classifier was fitted to detect whether an online comment is a `Cyber-Troll` or `Non Cyber-Troll`. This application
acts as an interface to allow any user to submit new queries to this model. 
  

## Installation

First clone the repo locally.
~~~bash
git clone https://github.com/wgopar/ml-flask-web-app.git
~~~

Create a new virtual environment in the project directory.
~~~bash
python3 -m venv ./venv
~~~

Activate the virtual environment.
~~~bash
source venv/bin/activate
~~~

While in the virtual environment, install required dependencies from `requirements.txt`.

~~~bash
pip install -r ./requirements.txt
~~~

Now we can deploy the web application via
~~~bash
python app.py
~~~

and navigate to `http://127.0.0.1:5000/` to see it live. On this page, a user can then submit text into the text 
field and receive predictions from the trained model and determine if the text most likely came from a `Cyber Troll` or 
`Non Cyber-Troll`.

The application may then be terminated with the following commands.
~~~bash
$ ^C           # exit flask application (ctrl-c)
$ deactivate   # exit virtual environment
~~~

## Project Structure 

~~~
ml-flask-web-app
├── model_assets
│   ├── model.pkl
│   └── vectorizer.pkl
├── model_dev
│   ├── data
│   |   └── data.json
│   └── model_dev.ipynb
├── templates
│   └── index.html
├── app.py
├── utils.py
├── requirements.txt
└── README.md
~~~

### detailed

`/model_assets` is used to store persisted states of the predictive model and learned feature extractors from scikit-learn. 

`/model_dev` is used as the model development playground where an `.ipynb` is used to develop the model and save new versions of persisted states.

Storing new persisted states of the model can be done within the jupyter notebook. As an example, within `model_dev.ipynb`
I can create a new model/retrain and include in into the `./model_assets` folder when I am satisfied. A simple example:

~~~~python
import utils

clf = LogisticRegression()
clf.fit(X_train, y_train)
utils.persist_model(clf, description='clf_v.0.0')  # creates clf_v.0.0.pkl in /model_assets folder
~~~~

Selecting the version of models to use during run time is chosen within the POST request function inside
in `app.py`.

`/templates` holds the html templates for the application.

