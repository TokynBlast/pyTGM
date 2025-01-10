"""
Exposes ecryptions
"""
from .hk32 import * #pylint:disable=import-error
from .b64 import Table, encode, decode
from .sha256 import encode as sha256

class hk32:
    @staticmethod
    def encode(data, key):
        hk32.encode()
    @staticmethod
    def decode(data, key):
        hk32.decode()

__all__ = ['Table', 'sha256', 'encode', 'decode', 'hk32.encode', 'hk32.decode']
