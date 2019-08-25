# ml-flask-web-app 



This is a simple web application using flask for interaction with a machine learning model
and obtain predictions from user input.  

(In progress...)
  

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

While in the virtual envirobment, install required dependences from `requirements.txt`.

~~~bash
pip install -r ./requirements.txt
~~~

Now we can deploy the web application via
~~~bash
python app.py
~~~

and navigate to `http://127.0.0.1:5000/` to see it live.

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
