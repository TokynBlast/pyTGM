""" Imports all files needed for terminal """

RESET = "\x1b[0m"

BOLD = '\x1b[1m'
ITALIC = '\x1b[3m'
UNDERLINE = '\x1b[4m'

__all__ = ['geky',
           'cls', 'color', 'pos',
           'RESET', 'ITALIC', 'BOLD', 'UNDERLINE']

def __getattr__(name):
    if name in __all__:
        return __import__(f"pyTGM.terminal.{name}", fromlist=[name])
    raise AttributeError(f"module {__name__} has no attribute {name}")
