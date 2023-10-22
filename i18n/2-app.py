#!/usr/bin/env python3
"""Get locale from request"""
from flask import Flask, render_template, request
from flask_babel import Babel

babel = Babel()

app = Flask(__name)
app.config.from_object('config.Config')


class Config:
    LANGUAGES = ["en", "fr"]

    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
