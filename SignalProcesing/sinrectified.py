#importar las librerias
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-4, 4, 100)#Crear el vector X
s = np.sin(x)#definir el vector X a partir de la funcion seno de numpy
s=abs(s)#"Rectificar los valores "
plt.plot(x, s)#plotear con los valores de x y s
plt.grid(True, which='both')#activar la grilla
plt.title('Sin rectified Signal')#añadir titulo
plt.show()#MOstrar el ploteo