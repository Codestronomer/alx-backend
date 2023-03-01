#!/usr/bin/env python3
"""
Module contains a simple flask app to demonstrate internalization
and localization in flask
"""
from flask import Flask, render_template

# initialize flask app
app = Flask(__name__)

# Home route ("/")
@app.route('/')
def hello_world():
    """
    defines a flask route that returns a template
    """
    return render_template('index.html')
