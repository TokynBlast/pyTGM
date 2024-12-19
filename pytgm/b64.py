"""
Dummy module for b64
"""

from .encrypt import b64

YELLOW = '\x1b[38;2;255;255;0m'
RED = '\x1b[38;2;255;0;0m'
RES = '\x1b[0m'
print(f'''{YELLOW}WARNING: {RED}b64 will be \
moved to ecrypt.b64 \
in v4.2.0{RES}''')

class Table:
    """
    Used for editing the table b64 uses to encode and decode.
    """
    table_ = b64.Table.table_

    @staticmethod
    def gen(chars=table_, times=1):
        """
        Dummy function
        """
        return b64.Table.gen(chars, times)

    def reset(): # pylint: disable=no-method-argument
        """
        Resets the table to the default
        """

        Table.table_ = '''ABCDEFGHIJKL \
MNOPQRSTUVWXYZabcdefghijk \
lmnopqrstuvwxyz1234567890?!@#$%^& \
*()_+-=[]{}\\|/,.<>~`;:'" '''


def encode(text):
    """
    Dummy function
    """
    return b64.encode(text)


def decode(text):
    """
    Dummy function
    """
    return b64.decode(text)
