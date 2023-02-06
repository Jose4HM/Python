import math
#Inductor
L=0.5e-6
#Resistecia
R=50
#Frecuencia
f=1
#Reactancia inductiva
Xl=2*math.pi*f*L
#Impedancia
Z=math.sqrt(R**2+Xl**2)
#Angulo
theta=math.atan(Xl/R)
#Frecuencia de corte
fc=R/(2*math.pi*L)
print("La frecuencia de corte es "+str(fc)+"Hz")
print("Impedancia: "+str(Z)+" Omega")
print("Ángulo: "+str(theta)+" rad")