#!/usr/bin/env python3
"""
hashing and validating passwords using the bcrypt
hashing algorithm
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Encrypting passwords"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str):
    """Check valid password"""
    try:
        hashed_password_str = hashed_password.decode('utf-8')

        return bcrypt.checkpw(password.encode('utf-8'),
                              hashed_password_str.encode('utf-8'))
    except (UnicodeDecodeError, ValueError):
        return False
