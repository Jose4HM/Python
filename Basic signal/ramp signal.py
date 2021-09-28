#Importar librerias
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
x=np.arange(-5,5,0.001)#Creación del vector x
m=3#Alcanze del valor estable
r_1=x>=0#Primer punto de elevación
r_2=x>=1#Punto de estabilizacion
r1=np.array(r_1)#Operaciones de vectpres
r1=r1*x*m#crecimiento del vector 
r2=np.array(r_2)
r2=r2*(x-1)*-m#Se resta el vector para que se pueda estabilizar en un número
rt=r1+r2#Se suman ambos vectores
plt.plot(x,rt)#PLotear
plt.show()#Mostrar

