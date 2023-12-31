#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = getenv("AUTH_TYPE")

if auth_type:
    if auth_type == "basic_auth":
        auth = BasicAuth()
    elif auth_type == "session_auth":
        auth = SessionAuth()
    else:
        from api.v1.auth.auth import Auth
        auth = Auth()


excluded_paths = ['/api/v1/auth_session/login/']

def require_authentication():
    """Requires authentication"""
    if auth is None:
        return
    if request.path not in excluded_paths and auth.require_auth(request.path, excluded_paths):
        if auth.authorization_header(request) is None and auth.session_cookie(request) is None:
            abort(401)


@app.before_request
def before_request():
    """return the current request"""
    require_authentication()
    request.current_user = auth.current_user(request)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error):
    """ Unauthorized handler """
    response = jsonify({"error": "Unauthorized"})
    response.status_code = 401
    return response


@app.errorhandler(403)
def forbidden(error):
    """ Forbidden handler """
    response = jsonify({"error": "Forbidden"})
    response.status_code = 403
    return response


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
