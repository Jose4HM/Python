import numpy as np
import matplotlib.pyplot as plt
from scipy import signal 
#codigo
t = np.linspace(0, 3, 1800)
pwm=np.zeros(len(t))
fc = 9
fm = 3
a = 10
b = 6
c=0.3
#señal
vm = b*(np.sin(2*np.pi*fm*t))*np.exp(-1*c*t)
vc = a*(signal.sawtooth(2*np.pi*fc*t))
#codigo
n = len(vc)
for i in range (1,n):
    if vm[i] <= vc[i]:
        pwm[i] = 1
    else:
        pwm[i] = 0

fig, (ax1, ax2, ax3) = plt.subplots(3)
ax1.plot(t,vm)
ax2.plot(t,vc)
ax3.plot(t,pwm)
ax1.title.set_text('Modulating signal')
ax2.title.set_text('Carrier signal')
ax3.title.set_text('PWM signal')
ax1.grid(True, which='both')#activar la grilla
ax2.grid(True, which='both')#activar la grilla
ax3.grid(True, which='both')#activar la grilla
plt.tight_layout()
plt.show()