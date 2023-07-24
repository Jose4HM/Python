import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(1, 100, 1000)
x_volts = 10 * np.sin(t / (2 * np.pi))

plt.subplot(3, 1, 1)
plt.plot(t, x_volts)
plt.title('Signal')
plt.ylabel('Voltage (V)')
plt.xlabel('Time (s)')

x_watts = x_volts ** 2

plt.subplot(3, 1, 2)
plt.plot(t, x_watts)
plt.title('Signal Power')
plt.ylabel('Power (W)')
plt.xlabel('Time (s)')

x_db = 10 * np.log10(x_watts)

plt.subplot(3, 1, 3)
plt.plot(t, x_db)
plt.title('Signal Power in dB')
plt.ylabel('Power (dB)')
plt.xlabel('Time (s)')

# Adjust spacing between subplots
plt.subplots_adjust(hspace=1)

plt.show()
