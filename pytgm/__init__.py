""" The init file for the pyTGM library """

__all__ = ['server', 'sound', 'rect']


def __getattr__(name):
    if name in __all__:
        return __import__(f"pytgm.{name}", fromlist=[name])
    raise AttributeError(f"module {__name__} has no attribute {name}")



__url__ = 'https://github.com/TokynBlast/pyTGM'
__download_url__ = 'https://pypi.org/tokynblast'
__bug_tracker_url__ = 'https://github.com/TokynBlast/pyTGM/issues'
__changelog_url__ = 'https://github.com/TokynBlast/pyTGM/blob/main/CHANGELOG.txt'