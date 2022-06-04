import csv
from traceback import print_tb
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from zmq import CURVE_SERVERKEY
def pretratamiento():
    archivo = 'E:/Archivos/Codes/Python/DataBase/2022a.xlsx'
    read_file = pd.DataFrame(pd.read_excel(archivo))
    read_file.to_csv('E:/Archivos/Codes/Python/DataBase/ExcelACSV.csv',index = None, header=True)
    df = pd.DataFrame(pd.read_csv('E:/Archivos/Codes/Python/DataBase/ExcelACSV.csv'))
    df=df.replace(np.nan, 0)
    Recorrer_cursos(df)
    MatrizPosibilidades(df)

def Recorrer_cursos(csvtratado):
    horariotmp = pd.read_csv('E:/Archivos/Codes/Python/DataBase/Horario.csv')
    cursos=csvtratado['ASIGNATURA'].unique()
    total_grupos=csvtratado['GRUPO'].unique()
    contadorArchivos=0
    for Inicializador in range(0,len(total_grupos)):
        CursosCompatibles=[]
        Grupo_especifico=Inicializador
        # print('Inicio de intento-------GRUPO:'+total_grupos[Grupo_especifico])
        horariotmp=pd.read_csv('E:/Archivos/Codes/Python/DataBase/Horario.csv')
        for Curso_especifico in range(0,len(cursos)):
            Coincidencia=False
            contador_interno=0
            while Coincidencia==False:
                # print('El contador interno es ' + str(contador_interno))
                # print('Se envio el grupo a la función '+total_grupos[Grupo_especifico])
                respuesta_horario=Ordenar(horariotmp,csvtratado,total_grupos,cursos,Curso_especifico,Grupo_especifico)
                if respuesta_horario[0]==True:
                    horariotmp=respuesta_horario[1]
                    CursosCompatibles.append(total_grupos[Grupo_especifico])
                    Grupo_especifico=0
                    contador_interno=-1
                    Coincidencia=True
                    # print('Compatible')
                else:
                    # print('Imcompatible')
                    if Grupo_especifico==len(total_grupos):
                        Grupo_especifico=0
                    else:
                        Grupo_especifico+=1
                        contador_interno+=1
                        if contador_interno==3:
                            # print('Salida de emergencia')
                            CursosCompatibles.append('No data')
                            Grupo_especifico=0
                            contador_interno=0
                            Coincidencia=True
        # horariotmp.to_csv('C:/Users/User/Desktop/Final/HorarioFinal{}.csv'.format(contadorArchivos), index = False, encoding='utf-8')
        # contadorArchivos=contadorArchivos+1
        # print(CursosCompatibles)

def MatrizPosibilidades(csvlisto):
    horariotmp = pd.read_csv('E:/Archivos/Codes/Python/DataBase/Horario.csv')
    cursos=csvlisto['ASIGNATURA'].unique()
    total_grupos=csvlisto['GRUPO'].unique()
    Numero_total_cursos=2#len(cursos)
    Numero_total_grupos=3#len(total_grupos)
    contador=0
    #Declaring an empty 1D array.
    a = []
    #Declaring an empty 1D array.
    b = []
    #Initialize the column.
    for j in range(0, Numero_total_cursos):
        b.append('')
    #Append the column to each row.
    for i in range(0, 3**Numero_total_cursos):
        a.append(b)
    mtx=np.array(a)
    for columnas in range(Numero_total_cursos-1,-1,-1):
        cont=0
        for filas in range(0,len(mtx),3**contador):
            mtx[filas,columnas]=total_grupos[cont]
            if cont<Numero_total_grupos:
                cont=0
            cont+=1
    print(mtx)
    


def Ordenar(horario,csvtratado,total_grupos,cursos,cada_curso,grupo):
    horarioReset=horario
    Dias=['Lunes','Martes','Miercoles','Jueves','Viernes']
    curso_unico=csvtratado.loc[csvtratado['ASIGNATURA'] == cursos[cada_curso]]#Seleccionamos solo una asignatura(los 3 grupos)
    Curso_unico_NoAsignaturaColumna=curso_unico.drop(['ASIGNATURA'], axis = 1)#Borramos la columna de asignatura
    SoloCurso_UnGrupo=Curso_unico_NoAsignaturaColumna.loc[Curso_unico_NoAsignaturaColumna['GRUPO'] == total_grupos[grupo]]#Seleccionamos un grupo en especifico, sin la columna de asigantura
    SoloCurso_UnGrupo_NOgrupoColumna=SoloCurso_UnGrupo.drop(['GRUPO'], axis = 1)#Borramos la columna de grupo
    HoraExacta=horario['Tiempo']
    for filas in range(0,len(SoloCurso_UnGrupo_NOgrupoColumna),2):
        limitadores=SoloCurso_UnGrupo_NOgrupoColumna.iloc[filas,0]#Analizamos cada elemento de la fila para saber si es un De: o un A:
        if limitadores=='De:':
            for RecorrerDias in range(1,6):#SI es un De: Hacemos que recorra para cada dia de la semana
                # print(RecorrerDias)
                DeATravesDias=SoloCurso_UnGrupo_NOgrupoColumna.iloc[filas,RecorrerDias]
                if DeATravesDias!=0:
                    verificador=False
                    idtiempoInicio=0
                    while verificador==False:
                        if HoraExacta[idtiempoInicio]==DeATravesDias:
                            verificador=True
                        else:
                            idtiempoInicio=idtiempoInicio+1
                    if horario.iloc[idtiempoInicio,horario.columns.get_loc(Dias[RecorrerDias-1])]=='Libre':
                        AaTravesDias=SoloCurso_UnGrupo_NOgrupoColumna.iloc[filas+1,RecorrerDias]
                        if AaTravesDias!=0:
                            verificador=False
                            idtiempoFinal=0
                            while verificador==False:
                                if HoraExacta[idtiempoFinal]==AaTravesDias:
                                    verificador=True
                                else:
                                    idtiempoFinal=idtiempoFinal+1
                            if horario.iloc[idtiempoFinal-1,horario.columns.get_loc(Dias[RecorrerDias-1])]=='Libre':
                                horario.iloc[idtiempoInicio,horario.columns.get_loc(Dias[RecorrerDias-1])]=cursos[cada_curso]+'('+total_grupos[grupo]+')'
                                horario.iloc[idtiempoInicio:idtiempoFinal,horario.columns.get_loc(Dias[RecorrerDias-1])]=cursos[cada_curso]+'('+total_grupos[grupo]+')'
                                # print('Devolvio con éxito')
                            else:
                                # print('Existe cruce final')
                                return(False,horarioReset)
                    else:
                        # print('Existe cruce inicial')
                        return(False,horarioReset)
    return(True,horario)
if __name__=="__main__":
    pretratamiento()