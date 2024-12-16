# pylint: disable=missing-module-docstring
from os import name as n, system as sys

def cls():
    """
    Clears the terminal screen and resets the cursor to the top left.
    """
    if n == 'nt':
        sys('cls')
    elif n == 'posix':
        sys('clear')
    else:
        print('\033[H\033[J', end='')
