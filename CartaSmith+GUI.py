import tkinter as tk
from tkinter import ttk
import numpy as np
import math as mt
def calculos():
    Lambda=float(box_lambda.get())
    Z0=int(box_Z0.get())
    ZL=complex(box_ZL.get())#A+Bj
    Vol=float(box_V.get())
    bl=2*np.pi*Lambda
    Zin=Z0*((ZL+Z0*1j*mt.tan(bl))/(Z0+ZL*1j*mt.tan(bl)))
    coef=(ZL-Z0)/(ZL+Z0)
    SWR=(1+abs(coef))/(1-abs(coef))
    rl=20*mt.log10(abs(coef))
    pr=(abs(coef)**2)*Vol
    tag_zin.config(text=f"Impedancia de entrada: {Zin}")
    tag_coefReflex.config(text=f"Coeficiente de reflexión: {abs(coef)}")
    tag_swr.config(text=f"SWR: {SWR}")
    tag_RL.config(text=f"Pérdida por retorno: {rl}")
    tag_RLP.config(text=f"Perdida por retorno-Potencia: {pr}")
ventana = tk.Tk()
#Titulo de la ventana
ventana.title("Smith Calculator")
#Tamaño de la ventana
ventana.config(width=400, height=300)
#================================================
#Textos de entrada
#================================================
#Input de texto de lambda
lambdaVar = ttk.Label(text="Longitud de onda (Lambda):")
#Posicion de texto lambda
lambdaVar.place(x=20, y=10)
#Input de texto de Z0
Z0Var = ttk.Label(text="Impedancia Caracteristica (Z0):")
#Posicion de texto Z0
Z0Var.place(x=20, y=40)
#Input de texto de ZL
ZLVar = ttk.Label(text="Impedancia de Carga (ZL):")
#Posicion de texto ZL
ZLVar.place(x=20, y=70)
#Input de texto de V
vVar = ttk.Label(text="Voltaje(V):")
#Posicion de texto V
vVar.place(x=20, y=100)
#================================================
#Cajas
#================================================
#Posicion de la caja de lambda
box_lambda = ttk.Entry()
box_lambda.place(x=200, y=10, width=60)
#Posicion de la caja de Z0
box_Z0 = ttk.Entry()
box_Z0.place(x=200, y=40, width=60)
#Posicion de la caja de ZL
box_ZL = ttk.Entry()
box_ZL.place(x=200, y=70, width=60)
#Posicion de la caja de V
box_V = ttk.Entry()
box_V.place(x=200, y=100, width=60)
#================================================
#Botón
#================================================
#Configuracion del boton para calcular
boton_convertir = ttk.Button(text="Calcular", command=calculos)
#Ubicacion del boton
boton_convertir.place(x=20, y=130)
#================================================
#Soluciones
#================================================
#Mostrar resultado: Impedancia de entrada
tag_zin = ttk.Label(text="Impedancia de entrada")
#Posicion de la impedancia de entrada
tag_zin.place(x=20, y=160)

#Mostrar coeficiente de reflexion
tag_coefReflex = ttk.Label(text="Coeficiente de reflexión:")
#Posición del coeficiente de reflexión
tag_coefReflex.place(x=20, y=190)

#Mostrar coeficiente de SWR
tag_swr = ttk.Label(text="SWR:")
#Posición del coeficiente de SWR
tag_swr.place(x=20, y=220)

#Mostrar coeficiente de RL
tag_RL = ttk.Label(text="Pérdida por retorno:")
#Posición del coeficiente de RL
tag_RL.place(x=20, y=250)

#Mostrar coeficiente de reflexion P
tag_RLP = ttk.Label(text="Perdida por retorno-Potencia:")
#Posición del coeficiente de reflexión P
tag_RLP.place(x=20, y=280)
ventana.mainloop()