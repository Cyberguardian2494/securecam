# modules/hasher.py

import hashlib

def hash_password(password: str) -> str:
    """
    Converts a plain text password to a SHA-256 hash.

    Args:
        password (str): The input password

    Returns:
        str: SHA-256 hex digest of the password
    """
    return hashlib.sha256(password.encode()).hexdigest()
