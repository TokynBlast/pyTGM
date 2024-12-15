"""
This module is used for encoding and decoding in base 64
A custom table can also be set
"""

from .random.seq.modify import shuffle as shuff

class Table:
    """
    Used for editing the table b64 uses to encode and decode.
    """
    table_ = '''ABCDEFGHIJKL \
MNOPQRSTUVWXYZabcdefghijk \
lmnopqrstuvwxyz1234567890?!@#$%^& \
*()_+-=[]{}\\|/,.<>~`;:'" '''

    @staticmethod
    def table_gen(chars, times):
        """
        Randomly generates a table to be used
        """
        if not chars:
            b64table = self.Table.table_
        else:
            b64table = chars

        self.table_ = shuff(self.table_, times)
        return b64table

def encode(text):
    """
    Encodes iputed data in b64, using the table_ var
    """
    bins = str()
    for c in text:
        bins += f'{int(bin(ord(c)), 2):08b}'
    while len(bins) % 3:
        bins += '00000000'
    for i in range(6, len(bins) + int(len(bins) / 6), 7):
        bins = bins[:i] + ' ' + bins[i:]
    bins = bins.split(' ')
    if '' in bins:
        bins.remove('')
    base64 = str()
    for b in bins:
        if b == '000000':
            base64 += '='
        else:
            base64 += self.table_[int(b, 2)]
    return base64

def decode(text):
    """
    Decodes encoded data in b64, using the table_ var
    """
    bins = str()
    for c in text:
        if c == '=':
            bins += '000000'
        else:
            bins += f'{int(bin(Table.table_.index(c)), 2):06b}'
    for i in range(8, len(bins) + int(len(bins) / 8), 9):
        bins = bins[:i] + ' ' + bins[i:]
    bins = bins.split(' ')
    if '' in bins:
        bins.remove('')
    text = str()
    for b in bins:
        if not b == '00000000':
            text += chr(int(b, 2))
    return text
