#importación de librerias
import numpy as np
import matplotlib.pyplot as plt
bits=[1, 1, 0, 0, 1, 0, 1]#bits de entrada
n=len(bits)#extraemos el tamaño del vector de bits
t=np.arange(0,n+0.01,0.01)#vector de tiempo
b_p=np.zeros(n)#pre- alojamos las variables
bw=np.zeros(100*(n)+1)#pre-alojamos las variables
for i in range(0,n):
    if bits[i]==0:#modulación bpsk
        b_p[i]=-1
    else:
        b_p[i]=1
    for j in range(10*i,10*(i+1)+1,1):
        bw[i*100:(i+1)*100]=b_p[i]#Igualamos cada segundo del tiempo a su equivalente: 1 y -1
sint=np.sin(2*np.pi*t)#Creamos nuestra moduladora de 1Hz
st=bw*sint#Multiplicamos el seno por cada valor(1 y -1), de modo que se invierte la fase
fig, (ax1, ax2, ax3) = plt.subplots(3)#Creamos los subplots
#Se plotea
ax1.plot(t,bw)
ax2.plot(t,sint)
ax3.plot(t,st)
ax1.title.set_text('Modulating signal')
ax2.title.set_text('Carrier signal')
ax3.title.set_text('PSK signal')
ax1.grid(True, which='both')#activar la grilla
ax2.grid(True, which='both')#activar la grilla
ax3.grid(True, which='both')#activar la grilla
plt.tight_layout()
plt.show()