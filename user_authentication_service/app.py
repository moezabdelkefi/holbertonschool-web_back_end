#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def hello_world():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register_user():
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        new_user = AUTH.register_user(email, password)

        response = {"email": new_user.email, "message": "user created"}
        return jsonify(response)
    except ValueError as err:
        response = {"message": str(err)}
        return jsonify(response), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
