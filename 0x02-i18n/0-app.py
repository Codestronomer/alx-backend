#!/usr/bin/env python3
"""
Module contains a simple flask app to demonstrate internalization
and localization in flask
"""
from flask import Flask, render_template


# initialize flask app
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    defines a flask route that returns a template
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0", debug=True)
