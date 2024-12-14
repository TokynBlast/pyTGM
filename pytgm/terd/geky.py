"""
Module for capturing keypresses, including arrow keys, on Windows and Unix-like systems.
"""

import sys
from tty import setraw
from termios import tcsetattr, TCSADRAIN, tcgetattr
from msvcrt import getch as win_getch


def geky(times=1):
    """
    Capture keypresses, supporting both Windows and Unix-like systems.

    Args:
        times (int): Number of keypresses to capture.

    Returns:
        str: Name of the key pressed, such as 'ArrowUp', 'space', or the character itself.
    """
    if sys.platform == 'win32':
        return _get_windows_keypress(times)
    else:
        return _get_unix_keypress(times)


def _get_windows_keypress(times):
    """
    Capture keypresses on Windows systems.

    Args:
        times (int): Number of keypresses to capture.

    Returns:
        str: Name of the key pressed.
    """
    for _ in range(times):
        key = win_getch()
        if key == b'\xe0':  # Arrow keys
            key = win_getch()
            return {
                b'H': 'ArrowUp',
                b'P': 'ArrowDown',
                b'K': 'ArrowLeft',
                b'M': 'ArrowRight',
            }.get(key, 'UnknownKey')
        return key.decode('utf-8', errors='ignore')


def _get_unix_keypress(times):
    """
    Capture keypresses on Unix-like systems.

    Args:
        times (int): Number of keypresses to capture.

    Returns:
        str: Name of the key pressed.
    """
    fd = sys.stdin.fileno()
    old_settings = tcgetattr(fd)

    try:
        setraw(fd)
        for _ in range(times):
            key = sys.stdin.read(1)
            if key == '\x1b':  # Arrow keys
                seq = sys.stdin.read(2)
                return {
                    '[A': 'ArrowUp',
                    '[B': 'ArrowDown',
                    '[C': 'ArrowRight',
                    '[D': 'ArrowLeft',
                }.get(seq, seq)
            elif key == ' ':
                return 'space'
            return key
    finally:
        tcsetattr(fd, TCSADRAIN, old_settings)
