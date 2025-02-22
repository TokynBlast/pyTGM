""" Exposes all patterns and animations """
from rect import *


__all__ = ['rect']


'''
def __getattr__(name):
    if name in __all__:
        return __import__(f"pyTGM.pattern.{name}", fromlist=[name])
    raise AttributeError(f"module {__name__} has no attribute {name}")
'''
