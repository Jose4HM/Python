#importar librerias
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-8,8,0.001)#creacion del vector x
y=np.zeros(len(x))#creacion de un vector de zeros, del mismo tamaño que x
for i in range(len(x)):#Bucle for que de acuerdo a un umbral 0 define los valores 0 y 1
    if x[i]>=0:#Si es mayor a 0, todos los valores seran cambiados a 1
        y[i]=1
    else:
        y[i]=0#Si es menor a 0, los valores seras siendo los mismos: ceros
plt.plot(x,y) #plotear
plt.grid(True, which='both')#activar las grillas
plt.title('Step unit signal')#Añadir un titulo
plt.show()#Mostrar el plot