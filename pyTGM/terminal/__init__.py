""" Imports all files needed for terminal """

import importlib
import sys

__all__ = ['geky', 'clear', 'color', 'pos',
           'RESET', 'ITALIC', 'BOLD', 'UNDERLINE', 'INVIS', 'BLINK']

RESET = "\x1b[0m"
BOLD = '\x1b[1m'
ITALIC = '\x1b[3m'
UNDERLINE = '\x1b[4m'
INVIS = '\x1b[8m'
BLINK = '\x1b[5m'

# Lazy-loading submodules
def __getattr__(name):
    if name in __all__:
        try:
            return importlib.import_module(f"{__name__}.{name}")
        except ImportError as e:
            raise ImportError(f"Could not import {name}: {e}") from e
    raise AttributeError(f"module {__name__} has no attribute {name}")


def __dir__():
    return list(__all__)
