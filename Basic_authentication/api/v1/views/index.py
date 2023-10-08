#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    return jsonify({"status": "OK"})

@app_views.route('/stats/', strict_slashes=False)
def stats():
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)

@app_views.route("/unauthorized", methods=["GET"])
def unauthorized_endpoint():
    abort(401)
