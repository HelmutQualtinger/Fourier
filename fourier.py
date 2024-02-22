
import numpy as np
import time
# Beispielvektor
vector = np.zeros(100)
# Fülle das Array x mit den Werten von 0 bis 10*pi in 100 Schritten
x = np.linspace(0, 10*np.pi, 20000)
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
amplitures1 = np.abs(fourier_transform1)

import matplotlib.pyplot as plt

# Plotte x über y
plt.subplot(2, 1, 1)
plt.plot(x, y, label='sine sumwave')
plt.plot(x, y1+0.05, label='square wave')
plt.plot(x, reconstructed_y+0.10,label='reconstructed sin sum wave  ')
plt.plot(x, reconstructed_y1+0.15,label='reconstructed square sumwave')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot von x über y')
plt.legend()  # Add this line to show the legend


# Plotte einen Bar-Chart der Amplituden
plt.subplot(2, 1, 2)
plt.bar(range(len(amplitudes)//8), amplitudes[:len(amplitudes)//8],2, label='Amplitudes')
plt.bar(range(1,len(amplitures1)//8+1), amplitures1[:len(amplitudes)//8],2, label='Amplitudes1')
plt.xlabel('Frequenz')
plt.ylabel('Amplitude')
plt.title('Bar-Chart der Amplituden')

plt.tight_layout()
plt.show()
