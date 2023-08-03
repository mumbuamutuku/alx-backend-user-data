#!/usr/bin/env python3
"""
Implement a hash_password function
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Generate a random salt and hash the password with the salt
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Hash the provided password with the same salt used for the hashed password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
