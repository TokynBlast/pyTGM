"""
This is the init file for the pyTGM library.

It imports and exposes various modules and functionalities for:
- File handling
- Graphics rendering
- Sound generation
- Base64 encoding/decoding
- Local server operations
"""

import .graphics

print(f'{graphics.color(255,255,0)}WARNING: file.read_line() will soon be \
{graphics.color(255,0,0)}depreciated!{graphics.RESET}')
print(f'{graphics.color(255,255,0)}WARNING: sound.generate will soon be \
{graphics.color(255,0,0)}depreciated!{graphics.RESET}\nAnd sound.play() will be renamed as sound()')

__all__ = [
    'Table', 'encode', 'decode',
    'read_line', 'mod_line',
    'play', 'generate',
    'cls', 'color', 'RESET', 'BOLD', 'ITALIC', 'UNDERLINE',
    'server', 'client',
]

__url__ = 'https://github.com/TokynBlast/pyTGM'
__homepage__ = 'https://pytgm.tokynblast.space/home'
__download_url__ = 'https://pypi.org/tokynblast'
__docs_url__ = 'https://pytgm.tokynblast.space/documentation/use'
__bug_tracker_url__ = 'https://github.com/TokynBlast/pyTGM/issues'
__source_code_url__ = 'https://github.com/TokynBlast/pyTGM/tree/main'
__changelog_url__ = 'https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt'

from pytgm import b64, file, sound, graphics, local_server, terd

# b64 Imports
from .b64 import Table, encode, decode

# File Imports
from .file import read_line, mod_line

# Sound Imports
from .sound import play, generate

# Graphics Imports
from .graphics import cls, color, RESET, BOLD, ITALIC, UNDERLINE

# Online Imports
from .local_server import server, client
