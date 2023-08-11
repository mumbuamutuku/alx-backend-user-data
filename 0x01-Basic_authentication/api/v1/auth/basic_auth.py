#!/usr/bin/env python3
"""
Basic Auth module
"""


from api.v1.auth.auth import Auth
import base64
import binascii
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    class BasicAuth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        returns the Base64 part of the Authorization header for a
        Basic Authentication
        Return None if authorization_header is None
        Return None if authorization_header is not a string
        Return None if authorization_header doesn’t start by Basic
        Otherwise, return the value after Basic (after the space)
        You can assume authorization_header contains only one Basic
        """
        if (authorization_header is None or
                not isinstance(authorization_header, str) or
                not authorization_header.startswith("Basic")):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        returns the decoded Base64 string base64_authorization_header:
        Return None if base64_authorization_header is None
        Return None if base64_authorization_header is not a string
        Return None if base64_authorization_header is not a valid Base64
        Otherwise, return the decoded value as UTF8 string
        - you can use decode('utf-8')
        """
        base64hd = base64_authorization_header
        if base64hd and isinstance(base64hd, str):
            try:
                encode = base64hd.encode('utf-8')
                base = base64.b64decode(encode)
                return base.decode('utf-8')
            except binascii.Error:
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        returns the user email and password from the Base64 decoded value.
        This method must return 2 values
        Return None, None if decoded_base64_authorization_header is None
        Return None, None if decoded_base64_authorization_header is not a str
        Return None, None if decoded_base64_authorization_header
        doesn’t contain :
        Otherwise, return the user email and the user password
        - these 2 values must be separated by a :
        can assume decoded_base64_authorization_header will contain only one
        """
        decd64 = decoded_base64_authorization_header
        if (decd64 and isinstance(decd64, str) and ":" in decd64):
            product = decd64.split(":", 1)
            return (product[0], product[1])
        return (None, None)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        returns the User instance based on his email and password.
        Return None if user_email is None or not a string
        Return None if user_pwd is None or not a string
        Return None if your database doesn’t contain any User instance with
        email equal to user_email
        - you should use the class method search of the User to lookup the
        list of users based on their email.
        Don’t forget to test all cases: “what if there is no user in DB?”, etc.
        Return None if user_pwd is not the password of the User instance found
        - you must use the method is_valid_password of User
        Otherwise, return the User instance
        """
        if not (user_email and isinstance(user_email, str) and
                user_pwd and isinstance(user_pwd, str)):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        overloads Auth and retrieves the User instance for a request:
        """
        header = self.authorization_header(request)
        b64header = self.extract_base64_authorization_header(header)
        decoded = self.decode_base64_authorization_header(b64header)
        usercreds = self.extract_user_credentials(decoded)
        return self.user_object_from_credentials(*usercreds)
