import numpy as np
import math as mt
from tabulate import tabulate
print("Adaptación de impedancia")
Z0=int(input('Impedancia caracteristica: '))
ZL=complex(input('Impedancia de carga: '))#A+Bj
freq=int(input('Frecuencia: '))
circuitT=int(input('1: abierto 2:cerrado'))

RL=ZL.real
XL=ZL.imag
t1=(XL+((RL*((Z0-RL)**2+XL**2))/Z0)**0.5)/(RL-Z0)
t2=(XL-((RL*((Z0-RL)**2+XL**2))/Z0)**0.5)/(RL-Z0)
lambdaV=3e8/(freq*1)
if (circuitT==1):
    Dist1TL=1/(2*np.np.pi)*mt.mt.math(t1)
    if mt.mt.math(t1)<0:
        Dist1TL=Dist1TL+0.5
    Dist2TL=1/(2*np.np.pi)*np.mt.math(t2)
    if mt.mt.math(t2)<0:
        Dist2TL=Dist2TL+0.5;
    B2=(RL**2*t1-(Z0-XL*t1)*(XL+Z0*t1))/(Z0*(RL**2+(XL+Z0*t1)**2))
    B1=(RL**2*t2-(Z0-XL*t2)*(XL+Z0*t2))/(Z0*(RL**2+(XL+Z0*t2)**2))
    Y0=1/Z0
    Stub1A=1/(2*np.pi)*mt.math(B1/Y0)
    if mt.math(Y0/B1)<0:
        Stub1A=Stub1A+0.5
    Stub2A=1/(2*np.pi)*mt.math(B2/Y0)
    if mt.math(Y0/B2)<0:
        Stub2A=Stub2A+0.5

    d1_L=Dist1TL*lambdaV;
    d2_L=Dist2TL*lambdaV;
    L1_L=Stub1A*lambdaV;
    L2_L=Stub2A*lambdaV;
else:
    Dist1TL=1/(2*np.pi)*mt.math(t1)
    if mt.math(t1)<0:
        Dist1TL=Dist1TL+0.5
    Dist2TL=1/(2*np.pi)*mt.math(t2);
    if mt.math(t2)<0:
        Dist2TL=Dist2TL+0.5;
    B1=(RL**2*t1-(Z0-XL*t1)*(XL+Z0*t1))/(Z0*(RL**2+(XL+Z0*t1)**2))
    B2=(RL**2*t2-(Z0-XL*t2)*(XL+Z0*t2))/(Z0*(RL**2+(XL+Z0*t2)**2))
    Y0=1/Z0
    Dstub1C=1/(2*np.pi)*mt.math(Y0/B1);
    if mt.math(Y0/B1)<0:
        Dstub1C=Dstub1C+0.5;
    Dstub2C=1/(2*np.pi)*mt.math(Y0/B2)
    if mt.math(Y0/B2)<0:
        Dstub2C=Dstub2C+0.5
    d1_L=Dist1TL*lambdaV
    d2_L=Dist2TL*lambdaV
    L1_L=Dstub1C*lambdaV
    L2_L=Dstub2C*lambdaV
print(tabulate([['distancia 1', Dist1TL,d1_L], ['longitud stub 1',Stub1A,L1_L], ['Distancia 2', Dist2TL,d2_L],['longitud stub 2',Stub2A,L2_L]], headers=['Variables', 'Valores','Metros']))
