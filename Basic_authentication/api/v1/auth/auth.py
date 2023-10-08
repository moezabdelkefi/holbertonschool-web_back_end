#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """class Auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a request requires authentication based on the path
        and a list of excluded paths.

        Args:
            path (str): The path of the request.
            excluded_paths (List[str]): A list of paths that do not require authentication.

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

            if path.startswith(excluded_path) or excluded_path.startswith(path):
                return False

        return True
