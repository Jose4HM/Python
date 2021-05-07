import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

adult=pd.read_csv('Parte 1/adult.csv',index_col=[0])

adultcld=adult.fillna(0)
adultcld=adultcld.replace('?','No data') #map({'?': 'No data'}) adultcld=adultcld['workclass'] si quieres solo cambiar una columna
adultcld.to_csv('Parte 1/adult_cleaned.csv')
ad=pd.read_csv('Parte 1/adult_cleaned.csv')
df=pd.DataFrame(ad)
df.head(10)#Visualizar datos
def main():
    try:
        print("Menu Analisis de datos")
        print("Se analiza el archivo Adultos \n")
        print("Opciones:")
        print(" 1)Visualizar el archivo")
        print(" 2)Ver estadisticas del archivo")
        print(" 3)Ver Agrupaciones")
        print(" 4)Ver graficas")
        a=int(input())
        menu1(a)
        
    except ValueError:
        main()
def menu1(a):
    if a ==1:
        print(ad)
        main()
    elif a==2:
        menudat()
    elif a==3:
        menugby()
    elif a==4:
        mengraf()

def menudat():
    print("Opciones")
    print(" 1)Tipos de datos\n 2)Tipos de datos numero\n 3)Tipo de datos objeto\n 4)Conteo de datos por columna\n 5)VAlor maximo\n 6)Valir minimo\n 7)Mediana\n 8)Menu\n")
    try:
        m=int(input())
        
        if m==1:
            dat(1)
        elif m==2:
            dat(2)
        elif m==3:
            dat(3)
        elif m==4:
            dat(4)
        elif m==5:
            dat(5)
        elif m==6:
            dat(6)
        elif m==7:
            dat(7)
        elif m==8:
            main()
        else:
            menudat()
    except ValueError:
        menudat()
        
def dat(o):
    if o==1:
        print(df.dtypes)
        menudat()
        
    elif o==2:
        print(df.select_dtypes(include=['number'])) #Mostraar solo los datos tipo numero
        menudat()
    elif o==3:
        print(df.select_dtypes(include=['object'])) #Mostraar solo los datos tipo objeto
        menudat()
        
    elif o==4:
        print(df.count()) #Conteo de datos de cada columna
        menudat()
        
    elif o==5:
        print(df.max()) #Valore maximos
        menudat()
        
    elif o==6:
        print(df.min()) #Valores minimos
        menudat()
        
    elif o==7:
        print(df.median()) #Mediana de cada columna solo tipo numero
        menudat()

        

def menugby():
    print("Opciones")
    print(" 1)Workclass\n 2)Education\n 3)Age\n 4)Marital\n 5)Sex\n 6)Native country\n 7)<50k >50k\n 8)Race\n 9)Menu\n")
    try:
        g=int(input())
        
        if g==1:
            gby(1)
        elif g==2:
            gby(2)
        elif g==3:
            gby(3)
        elif g==4:
            gby(4)
        elif g==5:
            gby(5)
        elif g==6:
            gby(6)
        elif g==7:
            gby(7)
        elif g==8:
            gby(8)
        elif g==9:
            main()
        else:
            menugby()
    except ValueError:
        menugby()
    
def gby(b):
    if b==1:
        wk=df.groupby(['workclass']).mean()
        print(wk)
        menugby()
        
    elif b==2:
        ed=df.groupby(['education']).mean()
        print(ed)
        menugby()
        
    elif b==3:
        ag=df.groupby(['age']).mean()
        print(ag)
        menugby()
        
    elif b==4:
        ma=df.groupby(['marital']).mean()
        print(ma)
        menugby()
        
    elif b==5:
        sx=df.groupby(['sex']).mean()
        print(sx)
        menugby()
        
    elif b==6:
        ct=df.groupby(['native_country']).mean()
        print(ct)
        menugby()
        
    elif b==7:
        fk=df.groupby(['label']).mean()
        print(fk)
        menugby()
        
    elif b==8:
        r=df.groupby(['race']).mean()
        print(r)
        menugby()
    
# ## Graficas
def mengraf():
    print("Opciones")
    print(" 1)Tipos de datos\n 2)Age's amount between men and women\n 3)Age vs Education num\n 4)Age's amount-hours per week\n 5)Total Workclass\n 6)Race\n 7)Sex by groups\n 8)Cantidad de datos por edades\n 9)Grade of education\n 10)Education's number\n 11)Marital situation\n 12)Occupation\n 13)Relatioship\n 14)Native country'\n 15)Hours per week\n 16)Education with capital gained\n 17)Menu principal")
    try:
        p=int(input())
            
        if p==1:
            plot(1)
        elif p==2:
            plot(2)
        elif p==3:
            plot(3)
        elif p==4:
            plot(4)
        elif p==5:
            plot(5)
        elif p==6:
            plot(6)
        elif p==7:
            plot(7)
        elif p==8:
             plot(8)
        elif p==9:
            plot(9)
        elif p==10:
            plot(10)
        elif p==11:
            plot(11)
        elif p==12:
            plot(12)
        elif p==13:
            plot(13)
        elif p==14:
            plot(14)
        elif p==15:
            plot(15)
        elif p==16:
            plot(16)
        elif p==(17):
            main()
        else:
            mengraf()
    except ValueError:
            mengraf()
            
def plot(op):
    if op==1:
        df.groupby('workclass')['age'].mean().plot(kind='bar',legend='Reverse',color=('red'),figsize=(20,10),fontsize=20)
        
        plt.ylabel=("Age's amount")
        plt.xlabel=('Workclass')
        plt.figtext(.3,.9,"Age's amount and kind of jobs",fontsize=30)
        plt.show()
        mengraf()

    elif op==2:#sex y promedio por edad
        df.age.groupby(df.sex).mean().plot(kind='pie',explode=(0,0.1),colors=('red','yellow'),autopct='%0.1f ',shadow=True,figsize=(20,10),fontsize=30)        
        plt.axis('equal')        
        plt.figtext(.45,.9,"Age's amount between men and women",fontsize=40)
        plt.show()
        mengraf()


    elif op==3: #dispersion:age-education_num
        ad.plot("education_num","age",kind="scatter",color='green',figsize=(20,10),fontsize=20)
        
        plt.figtext(.35,.9,"Age vs Education num",fontsize=40)
        plt.ylabel=("Education num")
        plt.xlabel=("Age")
        plt.show()
        mengraf()

    elif op==4:
        df.groupby('age')['hours_week'].mean().plot(kind='line',figsize=(20,10),color=('green'),fontsize=20)
        plt.grid(color='lightblue')
        plt.ylabel=('Hours per week')
        plt.xlabel=('Age')
        plt.figtext(.3,.9,"Age's amount-hours per week",fontsize=40)
        plt.show()
        mengraf()

        #Agrupaciones por columnas

    elif op==5:
        c1=np.arange(9,dtype=np.double)
        c=np.full_like(c1,0.05)
        df.groupby('workclass')['workclass'].count().plot(kind='pie',explode=c,autopct='%0.1f %%',figsize=(20,10),shadow=True,fontsize=20)
        plt.figtext(.3,.9,"Total workclass",fontsize=40)
        plt.axis('equal')
        plt.show()
        mengraf()

    elif op==6:
        d1=np.arange(5,dtype=np.double)
        d=np.full_like(d1,0.05)
        df.groupby('race')['race'].count().plot(kind='pie',autopct=('%0.1f %%'),cmap='jet',explode=d,shadow=True,figsize=(20,10),fontsize=15)
        plt.figtext(.45,.9,'Race',fontsize=40)
        plt.axis('equal')
        plt.ylabel=("Percentage per race")
        plt.show()
        mengraf()

    elif op==7:
        df.groupby('sex')['sex'].count().plot(kind='pie',autopct=('%0.1f %%'),cmap='viridis',explode=(0.1,0.1),shadow=True,figsize=(20,10),fontsize=30)
        plt.axis('equal')
        plt.figtext(.4,.9,'Sex by groups',fontsize=30)
        plt.ylabel=("Percentage per race")
        plt.show()
        mengraf()

    elif op==8:
        df.groupby('age')['age'].count().plot(kind='bar',figsize=(20,10),color=('purple'),fontsize=10)
        plt.figtext(.35,.9,'Cantidad de datos por edades',fontsize=30)
        plt.ylabel=("Total de datos")
        plt.xlabel=('Edades')
        plt.show()
        mengraf()

    elif op==9:
        df.groupby('education')['education'].count().plot(kind='bar',figsize=(20,10),color=('orange'),fontsize=20)        
        plt.figtext(.4,.9,'Grade of education',fontsize=30)
        plt.ylabel=("Total")
        plt.xlabel=('Grade of education')
        plt.show()
        mengraf()

    elif op==10:

        df.groupby('education_num')['education_num'].count().plot(kind='barh',figsize=(15,10),color=('crimson'),fontsize=20)
        plt.figtext(.35,.9,"Education's number",fontsize=30)
        plt.ylabel=("Grade")
        plt.xlabel=('Total')
        plt.show()
        mengraf()

    elif op==11:

        a1=np.arange(7,dtype=np.double)
        a=np.full_like(a1,0.05)
        
        df.groupby('marital')['marital'].count().plot(kind='pie',figsize=(20,10),autopct='%0.1f %%',cmap=('spring'),explode=a,shadow=True,fontsize=20)       
        plt.figtext(.5,.9,'Marital situation',fontsize=30)
        plt.show()
        mengraf()

    elif op==12:
        
        x=np.arange(15,dtype=np.double)
        k=np.full_like(x,0.1)
        df.groupby('occupation')['occupation'].count().plot(kind='pie',figsize=(20,10),cmap=('winter'),explode=k,shadow=True,autopct='%0.1f %%',fontsize=20)
        plt.figtext(.5,.9,'Occupation',fontsize=30)
        plt.show()
        mengraf()

    elif op==13:

        b=np.arange(6,dtype=np.double)
        b1=np.full_like(b,0.1)
        df.groupby('relationship')['relationship'].count().plot(kind='pie',figsize=(20,10),cmap=('winter'),explode=b1,shadow=True,autopct='%0.1f %%',fontsize=20)        
        plt.figtext(.5,.9,'Relatioship',fontsize=30)
        plt.ylabel=('')
        plt.show()
        mengraf()

    elif op==14:

        df.groupby('native_country')['native_country'].count().plot(kind='bar',fontsize=20,figsize=(20,10),color=('cyan'))        
        plt.figtext(.4,.9,'Native country',fontsize=30)
        plt.xlabel=('Country')
        plt.ylabel=('Sum')
        plt.show()
        mengraf()

    elif op==15:

        df.groupby('hours_week')['hours_week'].count().plot(kind='line',fontsize=20,figsize=(20,10),color=('gold'))
        plt.xlabel=('Hours')
        plt.ylabel=('NUmber of Persons')
        plt.figtext(.4,.9,'Hours per week',fontsize=30)
        plt.legend()
        plt.show()
        mengraf()

    elif op==16:

        df.groupby('education')['capital_gain'].mean().plot(kind='bar',fontsize=20,legend='Reverse',color=('green'),figsize=(15,10))      
        plt.figtext(.3,.9,'Education with capital gained',fontsize=30)
        plt.ylabel=('education')
        plt.xlabel=('capital gain')
        plt.show()
        mengraf()
        
        
if __name__ == "__main__":
    main()





