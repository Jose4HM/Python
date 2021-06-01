import pandas as pd
import numpy as np
import os 
from datetime import datetime
os.system('cls')
def clean():
    archivo = 'E:/Archivos/Codes/Python/DataBase/Horarios2021.xlsx'
    read_file = pd.DataFrame(pd.read_excel(archivo))
    read_file.to_csv('E:/Archivos/Codes/Python/DataBase/fileexcelhorarios(NoBorrar).csv',index = None, header=True)
    df = pd.DataFrame(pd.read_csv('E:/Archivos/Codes/Python/DataBase/fileexcelhorarios(NoBorrar).csv'))
    row=df.iloc[110:174]#las filas estan disminuidas en dos respecto al excel
    columns=row.iloc[:, 3:24]
    finaldata=columns.iloc[:, [0,1,4,15,16,17,18,19,20]] #
    final = finaldata.replace(np.nan, 0)
    final.columns=['Code','Signature','Group','Limits','Monday','Tuesday','Wednesday','Thursday','Friday']
    final=final.drop(final[final['Code']==0].index)
    final.to_csv('E:/Archivos/Codes/Python/DataBase/horarios/subjects.csv',index=False)
    df=pd.DataFrame(pd.read_csv('E:/Archivos/Codes/Python/DataBase/horarios/subjects.csv'))
    for j in range(4,df.shape[1]):
        for i in range(0,df.shape[0]):
            if df.iloc[i,j]=='0':
                df.iloc[i,j]="00:00:00"
            else:
                df.iloc[i,j]=df.iloc[i,j]
    for k in range(4,df.shape[1]):
        df.iloc[:,k]=df.iloc[:,k].astype('datetime64[ns]')
    extract(df)

def extract(data):
    subjects=data['Signature'].unique()
    for i in range(0,len(subjects)):
        csv=data[data.Signature==subjects[i]]
        csv.to_csv('E:/Archivos/Codes/Python/DataBase/horarios/CursosOnebyOne/subject{}.csv'.format(i+1),index=False)
    number=len(subjects)
    readall(number)

def readall(n):
    # for i in range(0,n):
    #     df=(pd.read_csv('C:/Users/User/Desktop/Codes/DataBase/horarios/CursosOnebyOne/subject{}.csv'.format(i+1)))
        # df = df.sort_values(by="Thursday")
    #     print(df)  

    df=(pd.read_csv('E:/Archivos/Codes/Python/DataBase/horarios/CursosOnebyOne/subject1.csv'))
    print(df["Monday"].sum())
    # print(df.sort_values(by="Thursday"))
    # print(df.dtypes)
if __name__=="__main__":
    clean()



    # for k in range(4,df.shape[1]):
    #     for h in range(0,df.shape[0]):
    #         df.iloc[h,k] = datetime.strptime(df.iloc[h,k],'%H:%M:%S').time()
    # df['Monday']=pd.to_datetime(df['Monday'], format='%H:%M:%S')
    # df['Monday'] = df['Monday'].astype('datetime64[ns]')