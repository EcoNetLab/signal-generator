import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import sys

def generate_sine_wave(frequency, duration, sample_rate = 44100):
    """
    Generate a sine wave.

    Parameters:
        frequency (float): Frequency in Hz.
        duration (float): Duration in seconds.
        sample_rate (int): Sampling rate in Hz.

    Returns:
        t (numpy.ndarray): Time axis in seconds.
        audio_signal (numpy.ndarray): Generated sine wave.
    """

    print(f"Frequency: {frequency} Hz, Duration: {duration} seconds")

    # Generate time axis
    t = np.linspace(
        0, duration,
        int(sample_rate * duration),
        endpoint=False
    )

    # Generate sine wave
    audio_signal = 0.5 * np.sin(2 * np.pi * frequency * t)

    return t, audio_signal

# Input parameters
frequency = float(sys.argv[1]) # Frequency in Hz
duration = float(sys.argv[2])  # Duration in second

# Signal
frequency = 250
duration = 10
t, signal = generate_sine_wave(frequency, duration)

# Write to wav file
write(
    "sin-waves/{}seconds-{}Hz.wav".format(duration, frequency),
    int(1/(t[1]-t[0])),
    signal.astype(np.float32)
)
