#importar librerias
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0, 1, 1000, endpoint=True)#crear vector tiempo
plt.plot(t, 5*(1+signal.square(2 * np.pi * 3 * t)))#General la señalcuadrada, 1+(desplazamiento vertical) y 5* escalamiento. 2*np.pi periodo
plt.title('Square wave')#Crear titulo
plt.xlabel('Time')#Añadir titulo al eje x
plt.ylabel('Amplitude')#Añadir titulo al eje y
plt.grid(True, which='both')#Mostrar grillas
plt.ylim(-1, 11)#Limitar el ploteo
plt.show() #Mostrar la grafica
