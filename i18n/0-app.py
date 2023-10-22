#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template
from os import getenv

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    return render_template('index.html')


if __name__ == '__main__':
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
