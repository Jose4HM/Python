import math
#Capacitor
C=25e-12
#Resistecia
R=50
#Frecuencia
f=1
#Reactancia capacitiva
Xc=1/(2*math.pi*f*C)
#Impedancia
Z=math.sqrt(R**2+Xc**2)
#Angulo
theta=math.atan(Xc/R)
#Frecuencia de corte
fc=1/(2*math.pi*C*R)
print("La frecuencia de corte es "+str(fc)+" Hz")
print("Impedancia: "+str(Z)+" Omega")
print("Ángulo: "+str(theta)+" rad")