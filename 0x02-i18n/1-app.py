#!/usr/bin/env python3
""" The Route module for the API """
from flask import Flask, request, render_template
from flask_babel import Babel
from os import getenv

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Defines the Babel configuration """
    LANGUAGES = ['en', 'fr']
    # these are the inherent defaults just btw
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# set the above class object as the configuration for the app
app.config.from_object('1-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ GET /
    Return:
      - 1-index.html
    """
    return render_template('1-index.html')
