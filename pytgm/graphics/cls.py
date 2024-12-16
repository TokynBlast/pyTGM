# pylint: disable=missing-module-docstring
from os import name, system as sys

def cls():
    """
    Clears the terminal screen and resets the cursor to the top left.
    """
    if name == 'nt':
        sys('cls')
    elif name == 'posix':
        sys('clear')
    else:
        print('\033[H\033[J', end='')
