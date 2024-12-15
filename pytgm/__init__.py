"""
Imports all modules for the library.
"""
__all__ = [
    'file', 'read_line', 'mod_line', 'graphics', 'cls',
    'color', 'res', 'Markup', 'bold', 'italic', 'underline',
    'terd', 'geky', 'click', 'sound', 'frequency', 'big', 'small',
    'board', 'boards', 'remove', 'modify', 'local_server', 'server',
    'client', 'b64', 'table_', 'table_gen', 'table_set', 'encode', 'decode'
]

__url__ = 'https://github.com/TokynBlast/pyTGM'
__homepage__ = 'https://pytgm.tokynblast.space/home'
__download_url__ = 'https://pypi.org/tokynblast'
__docs_url__ = 'https://pytgm.tokynblast.space/documentation/use'
__bug_tracker_url__ = 'https://github.com/TokynBlast/pyTGM/issues'
__source_code_url__ = 'https://github.com/TokynBlast/pyTGM/tree/main'
__changelog_url__ = 'https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt'

from pytgm import b64, file, board, sound, graphics, local_server, terd

# b64 Imports
from pytgm.b64 import Table, encode, decode
from pytgm.b64 import table_ as b64_table_, table_gen as b64_table_gen

# File Imports
from pytgm.file import read_line, mod_line

# Board Imports
from pytgm.board import boards, new, remove, modify

# Sound Imports
from pytgm.sound import play, generate

# Graphics Imports
from pytgm.graphics import cls, color, Markup, res
from pytgm.graphics.Markup import bold, italic, underline

# Online Imports
from pytgm.local_server import server, client

# terd Imports
from pytgm.terd import geky, click
