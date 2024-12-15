"""
Module for generating and playing sounds.

Includes functions for playing audio files and generating waveforms.
"""

import os
import wave
import math
import array
import sys


# Import PlaySound and SND_FILENAME only if available
if sys.platform == 'win32':
    try:
        from winsound import PlaySound as play_sound, SND_FILENAME
    except ImportError:
        play_sound = None
        SND_FILENAME = None
else:
    play_sound = None
    SND_FILENAME = None


def play(path):
    """
    Plays a sound from a given file path.

    Args:
        path (str): Path to the audio file.
    """
    if play_sound and SND_FILENAME:
        try:
            play_sound(path, SND_FILENAME)
        except Exception as e:  # pylint: disable=broad-exception-caught
            print(f"Error playing sound with winsound: {e}")
    else:
        try:
            if sys.platform == 'darwin':  # macOS
                os.system(f'afplay "{path}"')
            elif sys.platform.startswith('linux'):  # Linux
                os.system(f'aplay "{path}"')
            else:
                print("Sound playback is not supported on this platform.")
        except Exception as e:  # pylint: disable=broad-exception-caught
            print(f"Error playing sound: {e}")


def generate(frequency, duration, filename, sample_rate=44100, volume=0.5):
    """
    Generates a WAV file with a specific frequency and duration.

    Args:
        frequency (float): Frequency of the sound in Hz.
        duration (float): Duration of the sound in seconds.
        filename (str): Name of the output WAV file.
        sample_rate (int): Sampling rate in Hz (default: 44100).
        volume (float): Volume as a fraction of 1 (default: 0.5).
    """
    n_samples = int(sample_rate * duration)
    samples = array.array('h')

    for i in range(n_samples):
        t = i / sample_rate
        sample_value = volume * math.sin(2 * math.pi * frequency * t)
        samples.append(int(sample_value * 32767))

    try:
        with wave.open(filename, 'wb') as wave_file:
            wave_file.setnchannels(1)  # Mono
            wave_file.setsampwidth(2)  # 16-bit PCM
            wave_file.setframerate(sample_rate)
            wave_file.writeframes(samples.tobytes())
        print(f"Sound generated and saved to {filename}.")
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Error generating sound: {e}")
