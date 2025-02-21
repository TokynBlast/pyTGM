"""
Exposes ecryptions
"""

__all__ = ['hk512', 'b64', 'sha256']

def __getattr__(name):
    if name in __all__:
        return __import__(f"pyTGM.encrypt.{name}", fromlist=[name])
    raise AttributeError(f"module {__name__} has no attribute {name}")

