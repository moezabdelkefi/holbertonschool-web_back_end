#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify, request, abort, redirect
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


@app.route("/sessions", methods=["POST"])
def login() -> str:
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({
            "email": email,
            "message": "logged in",
            "session_id": session_id
        })
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"])
def logout() -> str:
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


@app.route("/profile", methods=["GET"])
def profile() -> str:
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        response = jsonify({"email": user.email})
        return jsonify(response, 200)
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'])
def reset_password():
    email = request.form.get('email')

    if not email:
        abort(403)

    try:
        reset_token = AUTH.get_reset_password_token(email)
        response = {"email": email, "reset_token": reset_token}
        return jsonify(response), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
