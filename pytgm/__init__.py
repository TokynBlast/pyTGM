""" The init file for the pyTGM library 


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
]"""
from . import sound
from . import local_server as server
from . import rect
__all__ = ['server', 'sound', 'rect']




__url__ = 'https://github.com/TokynBlast/pyTGM'
__download_url__ = 'https://pypi.org/tokynblast'
__bug_tracker_url__ = 'https://github.com/TokynBlast/pyTGM/issues'
__changelog_url__ = 'https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt'