"""
Moves the cursor to a determinate point
"""
def pos(X, Y, RET=True): # pylint: disable=missing-module-string
    if RET:
        '\033[X;YH'
    else:
        print('\033[X;YH)
