"""The init file for the pyTGM library"""
from . import sound as _sound
from . import rect as _rect

__all__ = ["sound", "rect"]

# Public aliases
sound = _sound
rect = _rect

__url__ = 'https://github.com/TokynBlast/pyTGM'
__download_url__ = 'https://pypi.org/tokynblast'
__bug_tracker_url__ = 'https://github.com/TokynBlast/pyTGM/issues'
__changelog_url__ = 'https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt'
