#!/usr/bin/env python3
"""
Implement a hash_password function
"""

import bcrypt


def hash_password(password):
    """
    Generate a random salt and hash the password with the salt
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
