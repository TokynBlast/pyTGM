"""
Encrypts in SHA256
"""

import hashlib

def encode(text):
    """
    Encodes the given text using SHA-256.
    
    Args:
        text (str): The input text to be encoded.
    
    Returns:
        str: The SHA-256 hash of the input text in hexadecimal format.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

    return hashlib.sha256().update(text.encode('utf-8')).hexdigest()
