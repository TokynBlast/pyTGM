"""
Module for generating and playing sounds.

Includes functions for playing audio files and generating waveforms.
"""

import os
import sys

# Import PlaySound and SND_FILENAME only if available
if sys.platform.startswith('Win32'):
    try:
        from winsound import PlaySound as PLAY_SOUND, SND_FILENAME
    except ImportError:
        PLAY_SOUND, SND_FILENAME = None, None
else:
    PLAY_SOUND, SND_FILENAME = None, None

def psound(path):
    """
    Plays a sound from a given file path.

    Args:
        path (str): Path to the audio file.
    """
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

def play(FPATH):
    psound(FPATH)
    YELLOW = '\x1b[38;2;255;255;0m'
    RED = '\x1b[38;2;255;0;0m'
    RES = '\x1b[0m'
    print(f'''{YELLOW}WARNING: {RED}sound.play() will become \
psound(str: file path) in 4.2.0\n
After that, sound.play() will no longer work.\n
If you want to play a sound, use psound(str: file path){RES}''')

def generate(p1=None, p2=None, p3=None, p4=None, p5=None): # pylint: disable=unused-argument
    del p1, p2, p3, p4, p5
    YELLOW = '\x1b[38;2;255;255;0m'
    RED = '\x1b[38;2;255;0;0m'
    RES = '\x1b[0m'

    print(f'''{YELLOW}WARNING: {RED}sound.generate() is no \
longer implemented
This change was made in 4.1.0., \
this function will be removed in 4.2.0
if you want to play a sound, use psound(str: file path){RES}''')
