""" Module Docstring """
from flask import Flask
APP = Flask(__name__)


@APP.route("/")
def hello():
    """ Function Docstring """
    return "Hello World!"


if __name__ == "__main__":
    APP.run()
