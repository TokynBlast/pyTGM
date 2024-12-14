"""
Used for detecting key presses
"""

def geky(times=1):  # pylint: disable=too-many-branches, too-many-return-statements
    """
    Gets a keyboard press, a determinate amount of times.
    """
    try:
        from msvcrt import getch as g  # pylint: disable=import-error
        for _ in range(times):
            k = g()
            if k == b'\xe0':
                k = g()
                if k == b'H':
                    return 'ArrowUp'
                elif k == b'P':  # pylint: disable=no-else-return
                    return 'ArrowDown'
                elif k == b'K':  # pylint: disable=no-else-return
                    return 'ArrowLeft'
                elif k == b'M':  # pylint: disable=no-else-return
                    return 'ArrowRight'
            else:  # pylint: disable=no-else-return
                return k.decode()

    except:
        from sys import stdin # pylint: disable=import-error,
        from tty import setraw # pylint: disable=import-error,
        from termios import tcsetattr, TCSADRAIN, tcgetattr # pylint: disable=import-error,
        for _ in range(times):
            fd = stdin.fileno()
            old = tcgetattr(fd)
            try:
                setraw(fd)
                c = stdin.read(1)
                if c == '\x1b':
                    c = stdin.read(2)
                    if c == '[A':
                        return 'ArrowUp'
                    elif c == '[B':  # pylint: disable=no-else-return
                        return 'ArrowDown'
                    elif c == '[C':  # pylint: disable=no-else-return
                        return 'ArrowRight'
                    elif c == '[D':  # pylint: disable=no-else-return
                        return 'ArrowLeft'
                    else:  # pylint: disable=no-else-return
                        return c
                else:
                    if c == ' ':
                        return 'space'
                    else:  # pylint: disable=no-else-return
                        return c
            finally:
                tcsetattr(fd, TCSADRAIN, old)
