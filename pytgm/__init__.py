"""
This is the init file for the pyTGM library.

It imports and exposes various modules and functionalities for:
- File handling
- Graphics rendering
- Sound generation
- Local server operations
"""

__all__ = [
    'Table', 'encode', 'decode',
    'sha256',
    'read_line', 'mod_line', 'fm_line',
    'play', 'generate', 'psound',
    'server', 'client',
]

__url__ = 'https://github.com/TokynBlast/pyTGM'
__homepage__ = 'https://pytgm.tokynblast.space/home'
__download_url__ = 'https://pypi.org/tokynblast'
__docs_url__ = 'https://pytgm.tokynblast.space/documentation/use'
__bug_tracker_url__ = 'https://github.com/TokynBlast/pyTGM/issues'
__source_code_url__ = 'https://github.com/TokynBlast/pyTGM/tree/main'
__changelog_url__ = 'https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt'

from pytgm import b64, file, sound, graphics, local_server, terd, encrypt

# b64 Imports
from .b64 import Table, encode, decode

# File Imports
from .file import read_line, mod_line, fm_line

# Sound Imports
from .sound import play, generate, psound

# Graphics Imports
from .graphics import cls, color, pos, RESET, BOLD, ITALIC, UNDERLINE

# Online Imports
from .local_server import server, client

# Ecnrypt Imports
from .encrypt import sha256, b64
