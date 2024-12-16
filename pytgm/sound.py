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
        from winsound import PlaySound as PLAY_SOUND, SND_FILENAME
    except ImportError:
        PLAY_SOUND, SND_FILENAME = None, None
else:
    PLAY_SOUND, SND_FILENAME = None, None


def play(path):
    """
    Plays a sound from a given file path.

    Args:
        path (str): Path to the audio file.
    """
    try:
        if PLAY_SOUND and SND_FILENAME:  # Windows
            PLAY_SOUND(path, SND_FILENAME)
        elif sys.platform == 'darwin':  # macOS
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


def generate(frequency, duration, filename, sample_rate=44100, volume=0.5):
    """
    Generates a sine wave and writes it to a WAV file.

    Args:
        frequency (float): Frequency of the sine wave in Hz.
        duration (float): Duration of the sound in seconds.
        filename (str): Name of the output WAV file.
        sample_rate (int): Sampling rate in Hz (default: 44100).
        volume (float): Volume as a fraction of 1 (default: 0.5).
    """
    # Input validation
    if not (20 <= frequency <= 20000):
        raise ValueError("Frequency must be between 20 Hz and 20,000 Hz.")
    if duration <= 0:
        raise ValueError("Duration must be greater than 0.")
    if not (0.0 <= volume <= 1.0):
        raise ValueError("Volume must be between 0.0 and 1.0.")

    # Number of samples and waveform calculation
    num_samples = int(sample_rate * duration)
    max_amplitude = int(32767 * volume)
    samples = array.array('h', (
        int(max_amplitude * math.sin(2 * math.pi * frequency * t / sample_rate))
        for t in range(num_samples)
    ))

    # Write samples to a WAV file
    try:
        with wave.open(filename, 'wb') as wave_file:
            wave_file.setnchannels(1)  # Mono audio
            wave_file.setsampwidth(2)  # 16-bit samples
            wave_file.setframerate(sample_rate)
            wave_file.writeframes(samples.tobytes())
        print(f"Sound generated and saved to {filename}.")
    except OSError as e:
        raise OSError(f"Failed to write file {filename}: {e}")
