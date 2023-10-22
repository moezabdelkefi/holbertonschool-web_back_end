#!/usr/bin/env python3
"""Parametrize templates"""
from flask import Flask, render_template, request
from flask_babel import Babel, _, gettext

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Returns the locale of the application"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
