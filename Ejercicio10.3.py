import math
#Inductor
L=0.05e-6
#Capacitor
C=25
#Resistencia
R=50
#Frecuencia de corte
w0=1/math.sqrt(L*C)
#Ancho de banda
WB=1/(R*C)
#Factor de calidad
Q=R*math.sqrt(C/L)
print("La frecuencia de corte es "+str(w0)+"rad/s")
print("El ancho de banda es: "+str(WB)+"Hz")
print("Factor de calidad: "+str(Q))