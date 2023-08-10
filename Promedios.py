import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

def on_window_configure(event):
    # Obtener el tamaño actual de la ventana
    ventana_ancho = root.winfo_width()
    ventana_alto = root.winfo_height()
    
    # Actualizar el tamaño de la figura en función del tamaño de la ventana
    fig.set_size_inches(ventana_ancho / 100, ventana_alto / 100)
    
    # Redibujar el gráfico en el canvas
    canvas.draw()


def obtener_datos(entries):
    matriz = []
    contador = 0
    for i in range(3):
        fila = []
        for j in range(4):
            valor = float(entries[contador].get())
            fila.append(valor)
            contador += 1
        matriz.append(fila)
    # print(matriz)
    checkpercent(matriz)
    return matriz


def main():
    # Crear ventana principal
    global root
    root = tk.Tk()
    root.title('Calculadora futuros posibles')
    #   Fijar el tamaño de la ventana y deshabilitar la redimensión
    root.geometry('900x700')
    entries = []
    
    # Etiquetas para los encabezados de columnas
    ttk.Label(root, text="E.C").grid(row=0, column=1, padx=25, pady=5)
    ttk.Label(root, text="Peso (%)").grid(row=0, column=2, padx=25, pady=5)
    ttk.Label(root, text="Exámen").grid(row=0, column=3, padx=25, pady=5)
    ttk.Label(root, text="Peso (%)").grid(row=0, column=4, padx=25, pady=5)

    # Etiquetas para los encabezados de filas
    ttk.Label(root, text="I").grid(row=1, column=0, padx=25, pady=5)
    ttk.Label(root, text="II").grid(row=2, column=0, padx=25, pady=5)
    ttk.Label(root, text="III").grid(row=3, column=0, padx=25, pady=5)


    # Crear y posicionar las entradas en una matriz de 3x4
    for i in range(3):
        for j in range(4):
            entry = ttk.Entry(root)
            entry.grid(row=i + 1, column=j + 1, padx=25, pady=5)
            entries.append(entry)

    # Botón para obtener los datos
    obtener_button = ttk.Button(root, text='Calcular', command=lambda: obtener_datos(entries))
    obtener_button.grid(column=4,row=4, columnspan=4, padx=5, pady=10)
    # Ejecutar el ciclo principal de la aplicación
    root.mainloop()


def checkpercent(grades):
    onehundred=0
    for i in range(0,3,1):
        for j in range(1,4,2):
            onehundred=onehundred+grades[i][j]
    if onehundred!=100:
        messagebox.showwarning('Advertencia', 'Los porcentajes no suman 100%')
    else:
        # print(onehundred)
        multiverse(grades)

def multiverse(grades):
    e=2
    grade1=[]
    grade2=[]
    if grades[2][0]!=0 and grades[2][2]!=0:
        messagebox.showinfo('Información', 'Promedio de: '+str(checkApprove(grades)))
    
    elif grades[2][0]!=0:
            for k in range(0,21,1):
                grades[e][0]=grades[2][0]
                grades[e][2]=k
                if checkApprove(grades)>=10.5:
                    grade1.append(grades[2][0]) #Continua
                    grade2.append(k) #Examen

    elif grades[2][2]!=0:
        for l in range(0,21,1):
                grades[e][0]=l
                grades[e][2]=grades[2][2]
                if checkApprove(grades)>=10.5:
                    grade1.append(l) #Continua
                    grade2.append(grades[2][2]) #Examen
    
    else:    
        for l in range(0,21,1):
            for k in range(0,21,1):
                grades[e][0]=l
                grades[e][2]=k
                if checkApprove(grades)>=10.5:
                    grade1.append(l) #Continua
                    grade2.append(k) #Examen
        
    plot_graph(root,grade1,grade2)

def checkApprove(mgrades):
    promt = 0
    for eva in [0, 1, 2]:
        for grade in [0, 2]:
            promt += mgrades[eva][grade] * (mgrades[eva][grade+1] / 100)
    return promt

def plot_graph(root,x,y):
    global fig, canvas

    fig = Figure(figsize=(root.winfo_width() / 100, root.winfo_height() / 100), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(x, y, label='Vector 1')
    ax.set_title('Cuanto necesito para aprobar?')
    ax.set_xlabel('Ev. Continua')  # Añadir etiqueta al eje x
    ax.set_ylabel('Exámen')  # Añadir etiqueta al eje x
    ax.grid(True)  # Activar las retículas

    # Cambiar ticks del eje x e y
    custom_xticks = range(0, 21, 1)  # Cambiar estos valores según tus preferencias
    custom_yticks = range(0, 21, 1)  # Cambiar estos valores según tus preferencias
    ax.set_xticks(custom_xticks)
    ax.set_yticks(custom_yticks)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(row=4, columnspan=4, padx=10, pady=10)

    root.grid_rowconfigure(4, weight=1)  # Expansión vertical
    root.grid_columnconfigure(0, weight=1)  # Expansión horizontal


if __name__== '__main__':
    main()