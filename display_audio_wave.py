
import numpy as np
import time
import pathlib as path
import webbrowser
import plotly.subplots as sp
from plotly.subplots import make_subplots
import plotly.graph_objects as go
# Read the mp3 file and decode it
from pydub import AudioSegment
audio = AudioSegment.from_file("recorded_audio.mp3", format="mp3")
decoded_audio = audio.get_array_of_samples()
audio_array = np.array(decoded_audio)
pass


xtime = np.linspace(0, 10, len(audio_array))
fig_audio = go.Figure()
obj1 = go.Scatter(x=xtime,
                  y=audio_array, name='Audio Array')
fig_audio.add_trace(obj1)
fig_audio.update_layout(
    xaxis_title='Index',
    yaxis_title='Amplitude',
    title='Audio Array Plot'
)
fig_audio.write_html('audio_array.html')

plot_file_audio = path.Path('audio_array.html').absolute()
webbrowser.get().open(plot_file_audio.as_uri())

import simpleaudio as sa

# Play the audio_array using simpleaudio
wave_obj = sa.WaveObject(audio_array.astype(np.int16), num_channels=1, bytes_per_sample=2, sample_rate=audio.frame_rate)
play_obj = wave_obj.play()

# Beispielvektor
# Fülle das Array x mit den Werten von 0 bis 10*pi in 100 Schritten

y = audio_array[:441000]
xtime= np.linspace(0,10,len(y))
# Führe die Fourier-Transformation durch
start=time.time()
fourier_transform=np.fft.rfft(y)
duration=time.time()-start
print(f"Duration {duration*1e6:.2f} microseconds")
reconstructed_y  = np.fft.irfft(fourier_transform)
# Berechne die Amplituden
amplitudes = np.abs(fourier_transform)


# Plotte x über y

fig = go.Figure()
obj2 = go.Scatter(x=xtime, y=reconstructed_y+100, name='reconstructed signal')
fig.add_trace(obj2)

fig.update_layout(
    xaxis_title='Time',
    yaxis_title='Amplitude',
    title='Signal',
    legend=dict(
        x=0.8,
        y=0.9,
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=12,
            color="black"
        ),
        bgcolor="LightSteelBlue",
        bordercolor="Black",
        borderwidth=1
    )
)


# Create a bar chart for amplitudes
fig_bar = go.Figure()
xfrequency=np.arange(len(amplitudes)/10)
obj3 = go.Scatter(x=xfrequency, y=amplitudes, name='Frequency')
fig_bar.add_trace(obj3)

fig_bar.update_layout(
    xaxis_title='Time',
    yaxis_title='Amplitude',
    title='Signal',
    legend=dict(
        x=0.8,
        y=0.9,
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=12,
            color="black"
        ),
        bgcolor="LightSteelBlue",
        bordercolor="Black",
        borderwidth=1
    )
)
# Update the x-axis and y-axis to be logarithmic
fig_bar.update_layout(
    xaxis_type="log",
    yaxis_type="log"
)

# Update the x-axis and y-axis titles
fig.update_layout(
    xaxis_title='Time (log scale)',
    yaxis_title='Amplitude (log scale)'
)

# Update the bar chart to have logarithmic y-axis
fig_bar.update_layout(
    yaxis_type="log"
)

# Update the y-axis title for the bar chart



fig.write_html('signal.html')
fig_bar.write_html('fourier.html')

plot_file = path.Path('signal.html').absolute()
webbrowser.get().open(plot_file.as_uri())

plot_file = path.Path('fourier.html').absolute()
webbrowser.get().open(plot_file.as_uri())

# Create a subplot with two columns
fig_subplots = sp.make_subplots(
    rows=2, cols=2, subplot_titles=("Input Signal", "Reconstructed Signal", "Fourier Transform"))

fig_subplots.add_trace(obj1, row=1, col=1)
fig_subplots.update_xaxes(title_text="Time", row=1, col=1)
fig_subplots.update_yaxes(title_text="Amplitude", row=1, col=1)

fig_subplots.add_trace(obj2, row=1, col=2)
fig_subplots.update_xaxes(title_text="Time", row=1, col=2)

fig_subplots.add_trace(obj3, row=2, col=1)
fig_subplots.update_xaxes(type="linear", row=2, col=1)
fig_subplots.update_yaxes(type="log", row=2, col=1)
fig_subplots.update_layout(title="Signal and Fourier Transform")


fig_subplots.write_html('all.html')
plot_file_subplots = path.Path('all.html').absolute()
webbrowser.get().open(plot_file_subplots.as_uri())
play_obj.wait_done()
