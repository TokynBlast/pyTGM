__all__ = ['random','num','integer','binary','choose','seq','modify','shuffle','duplicate','remove','file','read_line','mod_ine','graphics','cls','color','res','bold','italic','underline','terd','geky','click','sound','file','frequency','big','small','board','boards','add','remove','modify','local_erver','server','client','b64','table_','table_gen','table_set','encode','decode']
__url__ = 'https://github.com/TokynBlast/pyTGM'
__homepage__ = 'https://pytgm.tokynblast.space/home'
__download_url__ = 'https://pypi.org/tokynblast'
__docs_url__ = 'https://pytgm.tokynblast.space/documentation/use'
__bug_tracker_url__ = 'https://github.com/TokynBlast/pyTGM/issues'
__source_code_url__ = 'https://github.com/TokynBlast/pyTGM/tree/main'
__changelog_url__ = 'https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt'

from . import random, b64, file, board, sound, graphics, local_server, terd

# Random imports
from .random import num, seq
from .random.num import integer, binary
from random.seq.modify import shuffle, duplicate, remove
import .random.seq.modify

# b64 Imports
from .b64 import Table, encode, decode
from .b64.Table import table_, table_gen

# File Imports
from .file import read_line, mod_line

# Board Imports
from .board import boards, new, remove, modify

# Sound imports
from .sound import file, big, small

# Graphic imports
from .graphics import cls, color, markup, res
from .graphics.markup import bold, italic, underline

# Online imports
from .local_server import server, client

# terd imports
from .terd import geky, click
