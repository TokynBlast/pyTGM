"""
Module for generating and playing sounds.

Includes functions for playing audio files and generating waveforms.
"""

import os
import math
import sys
import struct

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
    Generates a sine wave sound and writes it to a WAV file without using wave module.

    Args:
        frequency (float): Frequency of the sine wave in Hz.
        duration (float): Duration of the sound in seconds.
        filename (str): Name of the output WAV file.
        sample_rate (int): Sampling rate in Hz (default: 44100).
        volume (float): Volume as a fraction of 1 (default: 0.5).

    Raises:
        ValueError: If frequency, duration, or volume are invalid.
        OSError: If file writing encounters an error.
    """
    # Validate inputs
    if not 20 <= frequency <= 20000:
        raise ValueError("Frequency must be between 20 Hz and 20,000 Hz.")
    if duration <= 0:
        raise ValueError("Duration must be greater than 0.")
    if not 0.0 <= volume <= 1.0:
        raise ValueError("Volume must be between 0.0 and 1.0.")

    # Calculate the number of samples and waveform
    num_samples = int(sample_rate * duration)
    max_amplitude = int(32767 * volume)
    samples = [
        int(max_amplitude * math.sin(2 * math.pi * frequency * t / sample_rate))
        for t in range(num_samples)
    ]

    # Write custom WAV file
    try:
        with open(filename, 'wb') as file:
            # Write RIFF header
            file.write(b'RIFF')
            file_size = 36 + len(samples) * 2  # 36 bytes header + sample data size
            file.write(struct.pack('<I', file_size))
            file.write(b'WAVE')

            # Write fmt subchunk
            file.write(b'fmt ')
            file.write(struct.pack('<I', 16))  # Subchunk1Size (16 for PCM)
            file.write(struct.pack('<H', 1))  # AudioFormat (1 for PCM)
            file.write(struct.pack('<H', 1))  # NumChannels (1 for mono)
            file.write(struct.pack('<I', sample_rate))  # SampleRate
            byte_rate = sample_rate * 2  # NumChannels * BitsPerSample / 8
            file.write(struct.pack('<I', byte_rate))  # ByteRate
            file.write(struct.pack('<H', 2))  # BlockAlign (NumChannels * BitsPerSample / 8)
            file.write(struct.pack('<H', 16))  # BitsPerSample

            # Write data subchunk
            file.write(b'data')
            file.write(struct.pack('<I', len(samples) * 2))  # Subchunk2Size
            for sample in samples:
                file.write(struct.pack('<h', sample))  # Write each sample as signed 16-bit PCM

        print(f"Sound generated and saved to {filename}.")
    except OSError as e:
        raise OSError(f"Failed to write file {filename}: {e}") from e
