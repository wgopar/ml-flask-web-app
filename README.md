# ml-flask-web-app 

This is a web application designed to show the project structure for a machine learning model deployed using flask. This project features a machine learning model that has been trained to detect whether or not an online comment is a `Cyber-Troll` or `Non Cyber-Troll`. This application acts as an interface for a user to submit new queries. The machine learning model was built using various features of scikit learn:

* Support Vector Machine (SVM)
* Bag-of-Words text representation (BoW)
* Grid Search + Cross Validation

Each of these components are developed within the project in an offline setting inside `/model_dev`. The SVM and BoW models will still be needed in a production or testing setting in order to be able to predict user-submitted queries, so they can be serialized via python's pickle functionality and stored within the `/model_assets` folder. 

In order to detect whether or not an online comment is from a cyber troll, you can deploy this application locally and submit queries to the machine learning model to recieve predictions through a simple user interface. The model was trained using the
Dataset for Detection of Cyber-Trolls ([see here](https://dataturks.com/projects/abhishek.narayanan/Dataset%20for%20Detection%20of%20Cyber-Trolls/)). This project emphasizes more the development process of creating deploy-friendly machine learning projects, rather than the creating of the predictive model itself.

The model development notebook is located [here](https://github.com/wgopar/ml-flask-web-app/blob/master/model_dev/model_dev.ipynb). 

You can also find a blog post that accompanies this repo [here](http://www.wmendozagopar.com/creating-and-deploying-a-machine-learning-project-with-flask.html#creating-and-deploying-a-machine-learning-project-with-flask).

Note that this project is still *in progress*

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

![Screen shot](/static/screen-shot-ui.png "User Interface")


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



[]: './static/screen-shot-ui.png'
