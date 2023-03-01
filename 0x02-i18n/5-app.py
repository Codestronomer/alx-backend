#!/usr/bin/env python3
"""
Module contains a simple flask app to demonstrate internalization
and localization in flask
"""
from flask import Flask, render_template, request, g
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
def get_locale():
    """
    gets the user's default locales and returns the best match
    """
    url_locale = request.args.get('locale')
    if url_locale in app.config['LANGUAGES']:
        return url_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Returns a user dictionary or None ID value can't be found or
    the 'login_as' url parameter was not found in request
    """
    id = request.args.get('login_as', None)
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """
    Add user to flask.g if user is found
    """
    user = get_user()
    g.user = user


@app.route('/', strict_slashes=False)
def home() -> str:
    """
    Flask application entry point
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0", debug=True)
