""" The init file for the pyTGM library """

import pyTGM.sound
import pyTGM.rect
import pyTGM.terminal
import pyTGM.encrypt

__all__ = [
    "terminal",
    "encrypt",
    "sound",
    "rect",
    "RESET",
    "ITALIC",
    "BOLD",
    "UNDERLINE",
    "INVIS",
    "BLINK",
]

RESET = "\x1b[0m"
BOLD = "\x1b[1m"
ITALIC = "\x1b[3m"
UNDERLINE = "\x1b[4m"
INVIS = "\x1b[8m"
BLINK = "\x1b[5m"


__url__ = 'https://github.com/TokynBlast/pyTGM'
__download_url__ = 'https://pypi.org/tokynblast'
__bug_tracker_url__ = 'https://github.com/TokynBlast/pyTGM/issues'
__changelog_url__ = 'https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt'
