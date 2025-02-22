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
from local_server import *
from sound import *
__all__ = ['local_server', 'sound']




__url__ = 'https://github.com/TokynBlast/pyTGM'
__download_url__ = 'https://pypi.org/tokynblast'
__bug_tracker_url__ = 'https://github.com/TokynBlast/pyTGM/issues'
__changelog_url__ = 'https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt'