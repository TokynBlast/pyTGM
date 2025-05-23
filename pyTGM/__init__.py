"""The initiation file""" #pylint:disable=invalid-name
import importlib

sound = importlib.import_module('.sound', __name__)
rect = importlib.import_module('.rect', __name__)

__all__ = ["sound", "rect"]

__url__ = 'https://github.com/TokynBlast/pyTGM'
__download_url__ = 'https://pypi.org/tokynblast'
__bug_tracker_url__ = 'https://github.com/TokynBlast/pyTGM/issues'
__changelog_url__ = 'https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt'
