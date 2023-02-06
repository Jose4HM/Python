#Calculadora de complejos
#Las operaciones trigonometricas aquí trabajan con radianes
#Importamos librerias
import math
import matplotlib.pyplot as plt
import numpy as np
#Registramos los valores del usuario, de debe ingresar un complejo como: a+bj
number=complex(input("Ingresa el número complejo: "))#Numero complejo
orden=int(input("Orden de la raiz: "))#Orden de la raiz
k=orden#Limite para la iteracion
if number.real==0:#Si la parte real es 0 se hacen excepciones para la indeterminacion
    if number.imag==0:
        theta=0
    elif number.imag>0:
        theta=math.pi/2
    elif number.imag<0:
        theta=3*math.pi/2
else:
    theta=math.atan(number.imag/number.real)#Thera calculada usando un arctg
valor=[]#Array de respuestas
#Bucle de iteracion
for i in range(0,k,1):
    r1=(abs(number)**(1/orden))*(math.cos((theta+2*i*math.pi)/(orden))+1j*math.sin((theta+2*i*math.pi)/(orden)))#Se calcula la rpta para cada valor de k
    valor.append(np.around(r1,4))#Se añade la respuesta al vector de respuestas y se redondea, el numero despues de r1 indica la cantidad de decimales
    print("Respuesta con k="+str(i))#Se imprime las respuestas
    print("------------------")
    print(valor[i])
    print("+++++++++++++++++++")
# Extraemos la parte real
x = [index.real for index in valor]
# Extraemos la parte imaginaria
y = [index.imag for index in valor]
ax = plt.gca()#Obtenemos las propiedades del plot
# plot the complex numbers
plt.scatter(x, y)#Ploteamos los puntos
plt.plot(x,y,color='b',zorder=1)#Unimos los puntos
plt.ylabel('Imaginary')#Rotulo de los ejes
plt.xlabel('Real')
plt.grid()#Activamos la grilla
for i_x, i_y in zip(x, y):#Obtenemos los valores para punto
    plt.text(i_x, i_y+0.02, '({}, j{})'.format(i_x, i_y))
plt.axvline(x=0, c="red")#Ploteamos los ejes del origen
plt.axhline(y=0, c="red")
plt.title("Raices complejas de "+str(number))#Añadimos titulos
plt.show()#Mostramos la grafica