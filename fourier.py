
import numpy as np
import time
import pathlib as path
import webbrowser
import plotly.subplots as sp
import plotly.graph_objects as go

# Beispielvektor
vector = np.zeros(100)
# Fülle das Array x mit den Werten von 0 bis 10*pi in 100 Schritten
x = np.linspace(0, 10*np.pi, 200)
y = np.sin(x) + 0.5*np.sin(3*x) + 0.25*np.sin(5*x) ## + 0.125*np.sin(7*x) + 0.0625*np.sin(9*x)
y1 = np.where(y > 0, 1, -1)
# Führe die Fourier-Transformation durch
start=time.time()
fourier_transform=np.fft.rfft(y)
fourier_transform1 = np.fft.rfft(y1)
duration=time.time()-start
print(f"Duration {duration*1e6:.2f} microseconds")
reconstructed_y  = np.fft.irfft(fourier_transform)
reconstructed_y1 = np.fft.irfft(fourier_transform1)
# Berechne die Amplituden
amplitudes = np.abs(fourier_transform)
amplitudes1 = np.abs(fourier_transform1)


# Plotte x über y
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, name='truncated sine sum wave'))
fig.add_trace(go.Scatter(x=x, y=y1+0.05, name='square wave'))
fig.add_trace(go.Scatter(x=x, y=reconstructed_y+0.10, name='reconstructed truncated sum wave'))
fig.add_trace(go.Scatter(x=x, y=reconstructed_y1+0.15, name='reconstructed square wave'))

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
fig_bar.add_trace(go.Bar(x=np.arange(len(amplitudes)), y=amplitudes, name='Truncated frequencies'))
fig_bar.update_layout(
    xaxis_title='Frequency',
    yaxis_title='Amplitude',
    title='Bar Chart of Frequencies'
)
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

offset = 0.5
# Create a bar chart for amplitudes1
fig_bar.add_trace(go.Bar(x=np.arange(len(amplitudes1))+offset, y=amplitudes1, name='All frequencies'))
fig_bar.update_layout(
    xaxis_title='Index',
    yaxis_title='Amplitude',
    title='Bar Chart ofFrequencies'
)

fig.write_html('signal.html')
fig_bar.write_html('fourier.html')

plot_file = path.Path('signal.html').absolute()
webbrowser.get().open(plot_file.as_uri())

plot_file = path.Path('fourier.html').absolute()
webbrowser.get().open(plot_file.as_uri())

# Create a subplot with two columns
fig_subplots = sp.make_subplots(rows=1, cols=2)

# Add the line plot to the first column
fig_subplots.add_trace(go.Scatter(
    x=x, y=y, name='truncated sine sumwave', legendgroup="group1"), row=1, col=1)
fig_subplots.add_trace(go.Scatter(x=x, y=y1+0.05, name='square wave'), row=1, col=1)
fig_subplots.add_trace(go.Scatter(x=x, y=reconstructed_y+0.10,
                       name='reconstructed truncated sin sum wave', legendgroup="group1"), row=1, col=1)
fig_subplots.add_trace(go.Scatter(x=x, y=reconstructed_y1+0.15,
                       name='reconstructed square sumwave', legendgroup="group1"), row=1, col=1)

# Add the bar chart to the second column
fig_subplots.add_trace(go.Bar(x=np.arange(len(amplitudes)), y=amplitudes,
                       name='Amplitudes', legendgroup="group2"), row=1, col=2)
fig_subplots.add_trace(go.Bar(x=np.arange(len(amplitudes1)+offset),
                       y=amplitudes1, name='Amplitudes1', legendgroup="group2"), row=1, col=2)

fig_subplots.update_xaxes(title_text="Time", row=1, col=1)
fig_subplots.update_yaxes(title_text="Amplitude", row=1, col=1)
fig_subplots.update_xaxes(title_text="Frequency", row=1, col=2)
fig_subplots.update_yaxes(title_text="Amplitude", row=1, col=2)


# Offset value for the second bar chart
offset = 1

fig_subplots.update_layout(
    title='Signal and Fourier Transform',
    legend=dict(
        x=0.8,
        y=1,
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=12,
            color="black"
        ),
        bgcolor="LightSteelBlue",
        bordercolor="Black",
        borderwidth=2
    ),    
)

fig_subplots.write_html('all.html')

plot_file_subplots = path.Path('all.html').absolute()
webbrowser.get().open(plot_file_subplots.as_uri())

fig_subplots.show()