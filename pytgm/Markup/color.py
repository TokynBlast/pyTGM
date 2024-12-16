# pylint: disable=missing-module-docstring
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
