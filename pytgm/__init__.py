"""
This is the init file for the pyTGM library.

It imports and exposes various modules and functionalities for:
- File handling
- Graphics rendering
- Local server operations
"""

__all__ = [
    'file_mod',
    'patt','line',

    'local_server',
    'server', 'client',

    'encrypt',
    'sha256', 'b64', 'hk512',

    'psound',

    'terminal',
    'cls', 'color', 'pos',
    'RESET', 'BOLD', 'UNDERLINE', 'ITALIC',
    'geky', 'click',

    'pattern',
    'rect'
]

__url__ = 'https://github.com/TokynBlast/pyTGM'
__download_url__ = 'https://pypi.org/tokynblast'
__bug_tracker_url__ = 'https://github.com/TokynBlast/pyTGM/issues'
__changelog_url__ = 'https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt'

from pytgm import encrypt, file_mod, sound, terminal, local_server, pattern #pylint: disable=import-self

# File Imports
from .file_mod import fm_line as line, rep as patt #pylint: disable=import-error

# Sound Imports
from .sound import psound # pylint: disable= import-error

# Graphics Imports
from .terminal import cls, color, pos, RESET, BOLD, ITALIC, UNDERLINE, geky, click #pylint:disable=import-error

# Online Imports
from .local_server import server, client

# Ecnrypt Imports
from .encrypt import sha256, b64, hk512 # pylint:disable=no-name-in-module

from .pattern import rect
