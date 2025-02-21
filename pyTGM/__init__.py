""" The init file for the pyTGM library """

__all__ = [
    'local_server',
    'server', 'client',

    'encrypt',
    'sha256', 'b64', 'hk512',

    'sound',

    'terminal',
    'clear', 'color', 'pos',
    'RESET', 'BOLD', 'UNDERLINE', 'ITALIC',
    'geky',

    'pattern',
    'rect'
]

__url__ = 'https://github.com/TokynBlast/pyTGM'
__download_url__ = 'https://pypi.org/tokynblast'
__bug_tracker_url__ = 'https://github.com/TokynBlast/pyTGM/issues'
__changelog_url__ = 'https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt'

from pytgm import encrypt, sound, terminal, pattern, local_server as server #pylint: disable=import-self

# Sound Imports
from .sound import sound # pylint: disable= import-error

# Graphics Imports
from .terminal import clear, color, pos, RESET, BOLD, ITALIC, UNDERLINE, geky #pylint:disable=import-error no-name-in-module

# Online Imports
from .local_server import server, client

# Ecnrypt Imports
from .encrypt import sha256, b64, hk512 # pylint:disable=no-name-in-module

from .pattern import rect
