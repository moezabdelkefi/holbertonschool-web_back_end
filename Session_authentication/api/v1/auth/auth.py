#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import request
from typing import List, TypeVar
from os import getenv

class Auth:
    """class Auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a request requires authentication based on the path
        and a list of excluded paths.

        Args:
            path (str): The path of the request.
            excluded_paths (List[str]): A list of paths that
            do not require authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None:
            return True

        if not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if not excluded_path.endswith('/'):
                excluded_path += '/'

            if path.startswith(excluded_path) or \
                    excluded_path.startswith(path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Extracts the authorization header from the Flask request.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            str: The authorization header value or None if not found.
        """
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user based on the Flask request.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            TypeVar('User'): The current user.
        """
        return None


    def session_cookie(self, request=None) -> str:
            """Get the value of the session cookie from a request.

            Args:
                request: The Flask request object.

            Returns:
                str: The value of the session cookie or None if not found.
            """
            if request is None:
                return None

            session_cookie_name = getenv("SESSION_NAME")
            if session_cookie_name is None:
                return None

            return request.cookies.get(session_cookie_name)
