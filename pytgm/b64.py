"""
This module is used for encoding and decoding in base64.
A custom table can also be set.
"""

from random import shuffle as shuff


class Table:
    """
    Used for editing the table b64 uses to encode and decode.
    """
    table_ = '''ABCDEFGHIJKL \
MNOPQRSTUVWXYZabcdefghijk \
lmnopqrstuvwxyz1234567890?!@#$%^& \
*()_+-=[]{}\\|/,.<>~`;:'" '''

    @staticmethod
    def gen(times=1, chars=Table.table_): # pylint: ignore: missing-module-docstring
        if not chars:
            b64table = Table.table_
        else:
            b64table = chars

        for _  in range:
            b64list = list(b64table)
            shuff(b64list)  # Fixed usage of `shuff` function
        return ''.join(b64list)  # Return the shuffled table


def encode(text):
    """
    Encodes inputted data in base64, using the table_ variable.

    Args:
        text (str): The text to encode.
    Returns:
        str: Encoded text in base64.
    """
    bins = str()
    for c in text:
        bins += f'{int(bin(ord(c)), 2):08b}'
    while len(bins) % 6:  # Ensure bins length is divisible by 6
        bins += '0'
    bins = [bins[i:i + 6] for i in range(0, len(bins), 6)]

    base64 = str()
    for b in bins:
        if b == '000000':
            base64 += '='
        else:
            base64 += Table.table_[int(b, 2)]
    return base64


def decode(text):
    """
    Decodes encoded data in base64, using the table_ variable.

    Args:
        text (str): The base64-encoded text to decode.
    Returns:
        str: Decoded text.
    """
    bins = str()
    for c in text:
        if c == '=':
            bins += '000000'
        else:
            bins += f'{int(bin(Table.table_.index(c)), 2):06b}'
    bins = [bins[i:i + 8] for i in range(0, len(bins), 8)]

    decoded_text = str()
    for b in bins:
        if b != '00000000':
            decoded_text += chr(int(b, 2))
    return decoded_text
