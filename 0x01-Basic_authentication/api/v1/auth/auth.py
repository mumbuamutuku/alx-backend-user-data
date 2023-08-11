#!/usr/bin/env python3
"""
Auth py
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """
    a class to manage the API authentication.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        returns True if the path is not in the list of strings excluded_paths:
        Returns True if path is None
        Returns True if excluded_paths is None or empty
        Returns False if path is in excluded_paths
        """
        checkpath = path
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """
        If request is None,returns None
        If request doesn’t contain the header key Authorization, returns None
        Otherwise, return the value of the header request Authorization
        """
        if request is None:
            return None
        request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns None - request will be the Flask request object
        """
        return None
