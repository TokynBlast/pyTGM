"""
Module for generating and playing sounds.

Includes functions for playing audio files and generating waveforms.
"""

import os
import wave
import math
import array
import sys

try:
    if sys.platform == 'win32':
        from winsound import PlaySound as PS, SND_FILENAME
except ImportError:
    PS = None
    SND_FILENAME = None

@staticmethod
def file(path):
    """
    Plays a sound at a given file location.
    """
    if PS and SND_FILENAME:
        try:
            PS(path, SND_FILENAME)
        except Exception as e:
            print(f"Error playing sound with winsound: {e}")
    else:
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
        wave_obj.setnchannels(1)  # Mono channel
        wave_obj.setsampwidth(2)  # 2 bytes per sample (16-bit PCM)
        wave_obj.setframerate(sample_rate)
        wave_obj.writeframes(samples.tobytes())
