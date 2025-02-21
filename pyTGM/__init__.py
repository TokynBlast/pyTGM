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

def __getattr__(name):
    if name in __all__:
        return __import__(f"pyTGM.encrypt.{name}", fromlist=[name])
    raise AttributeError(f"module {__name__} has no attribute {name}")