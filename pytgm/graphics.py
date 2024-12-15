"""
Used for markup on printed text, including styling and colors.
"""

import os

def cls():
    """
    Clears the terminal screen and resets the cursor to the top left.
    """
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    else:
        print('\033[H\033[J', end='')

def color(r, g, b):
    """
    Returns an ANSI escape code string to set text color using RGB values.

    Args:
        r (int): Red component (0-255).
        g (int): Green component (0-255).
        b (int): Blue component (0-255).

    Returns:
        str: ANSI escape code for the given RGB color.
    """
    return f"\x1b[38;2;{r};{g};{b}m"

RESET = "\x1b[0m"

# pylint: disable=too-few-public-methods
class Markup:
    """
    Contains ANSI escape codes for text styling (e.g., bold, italic, underline).
    """
    bold = '\x1b[1m'
    italic = '\x1b[3m'
    underline = '\x1b[4m'
