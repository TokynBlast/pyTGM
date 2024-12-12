def geky(times=1):
    try:
        from msvcrt import getch as g
        for i in range(times):
            k = g()
            if k == b'\xe0':
                k = g()
                if k == b'H':
                    return 'ArrowUp'
                elif k == b'P':
                    return 'ArrowDown'
                elif k == b'K':
                    return 'ArrowLeft'
                elif k == b'M':
                    return 'ArrowRight'
            else:
                return key.decode()

    except:
        from sys import stdin
        from tty import setraw
        from termios import tcsetattr, TCSADRAIN, tcgetattr
        for i in range(times):
            fd = stdin.fileno()
            old = tcgetattr(fd)
            try:
                setraw(fd)
                c = stdin.read(1)
                if c == '\x1b':
                    c = stdin.read(2)
                    if c == '[A': return 'ArrowUp'
                    elif c == '[B': return 'ArrowDown'
                    elif c == '[C': return 'ArrowRight'
                    elif c == '[D': return 'ArrowLeft'
                    else: return c
                else:
                    if c == ' ': return 'space'
                    else: return c
            finally: tcsetattr(fd, TCSADRAIN, old)
