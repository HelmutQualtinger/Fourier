import sounddevice as sd
import numpy as np
import tempfile
import os
from pydub import AudioSegment


def record_and_save_audio(filename, duration=10, sr=44100):
    print("Recording...")
    recording = sd.rec(int(duration * sr), samplerate=sr,
                       channels=1, dtype='int16')  # Record in mono
    sd.wait()
    print("Recording finished.")

    # Convert the recorded data to a suitable format for saving as an MP3
    audio_data = AudioSegment(
        recording.tobytes(),
        frame_rate=sr,
        sample_width=recording.dtype.itemsize,
        channels=1  # Mono
    )

    # Save the audio as an MP3 file with 128 kb/s bitrate
    audio_data.export(filename, format="mp3", bitrate="64k")

    print(f"Audio saved as {filename}")


if __name__ == "__main__":
    output_filename = "recorded_audio.mp3"
    record_and_save_audio(output_filename)
