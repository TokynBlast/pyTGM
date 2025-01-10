"""
This is the init file for the pyTGM library.

It imports and exposes various modules and functionalities for:
- File handling
- Graphics rendering
- Local server operations
"""

__all__ = [
    'file_mod', 'rep','fm_line',
    'psound',
    'local_server', 'server', 'client',
    'encrypt', 'sha256', 'b64', 'hk32',
    'psound',

    'terminal', 'cls', 'color', 'pos',
    'RESET', 'BOLD', 'UNDERLINE', 'ITALIC',
    'geky', 'click'
]

__url__ = 'https://github.com/TokynBlast/pyTGM'
__homepage__ = 'https://pytgm.tokynblast.space/home'
__download_url__ = 'https://pypi.org/tokynblast'
__docs_url__ = 'https://pytgm.tokynblast.space/documentation/use'
__bug_tracker_url__ = 'https://github.com/TokynBlast/pyTGM/issues'
__source_code_url__ = 'https://github.com/TokynBlast/pyTGM/tree/main'
__changelog_url__ = 'https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt'

from pytgm import encrypt, file_mod, sound, terminal, local_server #pylint: disable=import-self

# File Imports
from .file_mod import fm_line, rep #pylint: disable=import-error

# Sound Imports
from .sound import psound # pylint: disable= import-error

# Graphics Imports
from .terminal import cls, color, pos, RESET, BOLD, ITALIC, UNDERLINE, geky, click #pylint:disable=import-error

# Online Imports
from .local_server import server, client

# Ecnrypt Imports
from .encrypt import sha256, b64, hk32 # pylint:disable=no-name-in-module
