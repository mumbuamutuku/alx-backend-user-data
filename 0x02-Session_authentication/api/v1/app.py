#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

if getenv("AUTH_TYPE") == "auth":
    auth = Auth()
elif getenv("AUTH_TYPE") == "basic_auth":
    auth = BasicAuth()
elif getenv("AUTH_TYPE") == "session_auth":
    auth = SessionAuth


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    Add a new error handler for this status code, the response must be:
    a JSON: {"error": "Unauthorized"}
    status code 401
    you must use jsonify from Flask
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """
    Add a new error handler for this status code, the response must be:
    a JSON: {"error": "Forbidden"}
    status code 403
    you must use jsonify from Flask
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def authenticate_user():
    """
    if auth is None, do nothing
    if request.path is not part of this list ['/api/v1/status/',
    '/api/v1/unauthorized/', '/api/v1/forbidden/'], do nothing
    - you must use the method require_auth from the auth instance
    if auth.authorization_header(request) returns None,
    raise the error 401 - you must use abort
    if auth.current_user(request) returns None,
    raise the error 403 - you must use abort
    """
    if auth:
        excluded_paths = ['/api/v1/status/',
                          '/api/v1/unauthorized/',
                          '/api/v1/forbidden/',
                          '/api/v1/auth_session/login/',]
        if request.path not in excluded_paths:
        #if auth.require_auth(request.path, excluded_paths=excluded_paths):
            user = auth.current_user(request)
            if auth.authorization_header(request) is None:
                abort(401)
            if user is None:
                abort(403)
            request.current_user = user


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
