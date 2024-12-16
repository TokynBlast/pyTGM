# pylint: disable=missing-module-docstring, too-few-public-methods
class Markup:
    """
    Contains ANSI escape codes for text styling (e.g., bold, italic, underline).
    """
    bold = '\x1b[1m'
    italic = '\x1b[3m'
    underline = '\x1b[4m'
