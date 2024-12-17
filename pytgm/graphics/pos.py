"""
Moves the cursor to a determinate point
"""
def pos(x, y):  # pylint: disable=missing-function-docstring
    return f'\033[{x};{y}H'
