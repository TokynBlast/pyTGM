""" Exposes all patterns and animations """

__all__ = ['rect']


from rect import *

'''
def __getattr__(name):
    if name in __all__:
        return __import__(f"pyTGM.pattern.{name}", fromlist=[name])
    raise AttributeError(f"module {__name__} has no attribute {name}")
'''
