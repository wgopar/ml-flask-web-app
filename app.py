"""

Activate virtual environment that contains the packages in
requirements.txt


"""


from flask import Flask

app = Flask(__name__)

@app.route("/")
def first_func():
    return 'Hello World'


if __name__ == '__main__':
    app.run()