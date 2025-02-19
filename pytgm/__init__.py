"""
This is the init file for the pyTGM library.

It imports and exposes various modules and functionalities for:
- File handling
- Graphics rendering
- Local server operations
"""

__all__ = [
    'local_server',
    'server', 'client',

    'encrypt',
    'sha256', 'b64', 'hk512',

    'sound',
    'start', 'stop',

    'terminal',
    'cls', 'color', 'pos',
    'RESET', 'BOLD', 'UNDERLINE', 'ITALIC',
    'geky',

    'pattern',
    'rect'
]

__url__ = 'https://github.com/TokynBlast/pyTGM'
__download_url__ = 'https://pypi.org/tokynblast'
__bug_tracker_url__ = 'https://github.com/TokynBlast/pyTGM/issues'
__changelog_url__ = 'https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt'

from . import encrypt, sound, terminal, local_server, pattern

# Sound Imports
from .sound import start, stop # pylint: disable= import-error, no-name-in-module

# Graphics Imports
from .terminal import cls, color, pos, RESET, BOLD, ITALIC, UNDERLINE, geky #pylint:disable=import-error

# Online Imports
from .local_server import server, client

# Ecnrypt Imports
from .encrypt import sha256, b64, hk512 # pylint:disable=no-name-in-module

from .pattern import rect
