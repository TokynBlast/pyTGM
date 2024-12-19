"""
Module for generating and playing sounds.

Includes functions for playing audio files and generating waveforms.
"""

import os
import sys

def psound(path):
    """
    Plays a sound from a given file path.

    Args:
        path (str): Path to the audio file.
    """
    if sys.platform.startswith('Win'):
        try:
            from winsound import PlaySound as PLAY_SOUND, SND_FILENAME # pylint: disable=import-outside-toplevel
        except ImportError:
            PLAY_SOUND, SND_FILENAME = None, None # pylint: disable=invalid-name
    else:
        PLAY_SOUND, SND_FILENAME = None, None # pylint: disable=invalid-name

    try:
        if PLAY_SOUND and SND_FILENAME:  # Windows
            PLAY_SOUND(path, SND_FILENAME)
        elif sys.platform.startswith('darwin'):  # macOS
            os.system(f'afplay "{path}"')
        elif sys.platform.startswith('linux'):  # Linux
            os.system(f'aplay "{path}"')
        else:
            raise NotImplementedError("Sound playback is not supported on this platform.")
    except FileNotFoundError:
        print(f"Error: File not found - {path}")
    except OSError as e:
        print(f"Error playing sound: {e}")
    except NotImplementedError as e:
        print(e)

def play(fpath): # pylint: disable=missing-function-docstring
    psound(fpath)
    yellow = '\x1b[38;2;255;255;0m'
    red = '\x1b[38;2;255;0;0m'
    res = '\x1b[0m'
    print(f'''{yellow}WARNING: {red}sound.play() will become \
psound(str: file path) in 4.2.0
After that, sound.play() will no longer be a valid function.
If you want to play a sound, use psound(str: file path){res}''')

def generate(p1=None, p2=None, p3=None, p4=None, p5=None): # pylint: disable=unused-argument, missing-function-docstring
    del p1, p2, p3, p4, p5
    yellow = '\x1b[38;2;255;255;0m'
    red = '\x1b[38;2;255;0;0m'
    res = '\x1b[0m'

    print(f'''{yellow}WARNING: {red}sound.generate() is no \
longer implemented
This change was made in 4.1.0, \
this function will be removed entirley in 4.2.0
if you want to play a sound, use psound(str: file path){res}''')
