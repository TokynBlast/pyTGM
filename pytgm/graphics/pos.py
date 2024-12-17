"""
Moves the cursor to a determinate point
"""
def pos(X, Y, RET=True):  # pylint: disable=missing-module-string
    if RET:
        return f'\033[{X};{Y}H'
    else:
        print(f'\033[{X};{Y}H')
