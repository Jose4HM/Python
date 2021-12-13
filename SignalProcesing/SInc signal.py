#importación de librerias
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-4, 4, 100) #Vector x
vals = np.sinc(x)   #Definicion del vector "y" mediante una señal seno
plt.plot(x, vals)   #plotear la señal
plt.grid(True, which='both')    #Activar las grillas
plt.title('Sinc Signal')    #Crear titulos
plt.show()  #Mostrar la gráfica