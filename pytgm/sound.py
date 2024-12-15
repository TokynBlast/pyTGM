"""
Module for generating and playing sounds.

Includes functions for playing audio files and generating waveforms.
"""

import os
import wave
import math
import array
import sys

if sys.platform == 'win32':
    from winsound import PlaySound as PS, SND_FILENAME

@staticmethod
def file(path):
    """
    Plays a sound at a given file location.
    """
    try:
        PS(path, SND_FILENAME)
    except ImportError:
        try:
            if os.uname().sysname == 'Darwin':  # macOS
                os.system(f'afplay {path}')
            else:  # Linux
                os.system(f'aplay {path}')
        except AttributeError:
            pass

@staticmethod
def generate(frequency, duration, name, sample_rate=44100, volume=0.5):
    """
    Generates a WAV file with a specific frequency and duration.

    Args:
        frequency (float): Frequency of the sound in Hz.
        duration (float): Duration of the sound in seconds.
        name (str): Output WAV file name.
        sample_rate (int): Sampling rate in Hz (default: 44100).
        volume (float): Volume as a fraction of 1 (default: 0.5).
    """
    n_samples = int(sample_rate * duration)
    samples = array.array('h')

    for i in range(n_samples):
        t = i / sample_rate
        sample_value = volume * math.sin(2 * math.pi * frequency * t)
        samples.append(int(sample_value * 32767))

    with wave.open(name, 'wb') as wave_obj:
        num_channels = wave_obj.getnchannels()
        sample_width = wave_obj.getsampwidth()
        frame_rate = wave_obj.getframerate()
        wave_obj.setnchannels(num_channels)
        wave_obj.setsampwidth(sample_width)
        wave_obj.setframerate(frame_rate)
        wave_obj.writeframesraw(samples.tobytes())