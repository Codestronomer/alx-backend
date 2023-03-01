#!/usr/bin/env python3
"""
Module contains a simple flask app to demonstrate internalization
and localization in flask
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    object defines babel configuration for Flask application
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# initialize flask app
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    gets the user's default locales and returns the best match
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home() -> str:
    """
    Flask application entry point
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0", debug=True)
