import pydub
import numpy as np
from pydub import AudioSegment
import simpleaudio as sa


def play_mp3(file_path):
    try:
        audio = AudioSegment.from_mp3(file_path)
        # Convert to raw PCM data
        raw_data = audio.get_array_of_samples()
        # Get the sample width in bytes
        sample_width = audio.sample_width
        print("Sample width:", sample_width)
        # Get the number of channels
        channels = 1
        print("Audio channels",audio.channels)
        # Get the sample rate
        sample_rate = audio.frame_rate
        # Create a WaveObject
        wave_obj = sa.WaveObject(np.array(raw_data).astype(np.int16), audio.channels,sample_width)
        # Play the audio
        play_obj = wave_obj.play()
        # Wait until playback is finished
        play_obj.wait_done()
    except FileNotFoundError:
        print("File not found:", file_path)
    except Exception as e:
        print("Error occurred:", e)


# Replace 'your_file.mp3' with the path to your MP3 file
play_mp3('recorded_audio.mp3')
