import csv
import matplotlib.pyplot as plt
import numpy as np

def generar_onda_cuadrada_asimetrica(frecuencia, duracion_pulso, duracion_total):
    tiempo = np.linspace(-duracion_total, duracion_total, num=5952)
    periodo = 1 / frecuencia
    amplitud = 0.7
    voltaje_bajo = -0.3

    onda = []
    for t in tiempo:
        fase = t % periodo
        if fase < duracion_pulso:
            onda.append(amplitud)
        else:
            onda.append(voltaje_bajo)

    return tiempo, np.array(onda)

#Leer los archivos CSV y almacenar los datos en listas
archivos = ['C:/Users/Nitro/Desktop/Ruido/1.csv', 'C:/Users/Nitro/Desktop/Ruido/3.csv']
datos = []

for archivo in archivos:
    tiempo = []
    voltaje = []

    with open(archivo, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            tiempo.append(float(row[0]))
            voltaje.append(float(row[1]))

    datos.append((tiempo, voltaje))

frecuencia = 21.5  # Hz

duracion_pulso = 0.014  # segundos
duracion_total = 0.06  # segundos

tiempo, onda = generar_onda_cuadrada_asimetrica(frecuencia, duracion_pulso, duracion_total)
Ruido_intento=np.array(datos[1][1])-np.array(onda)
frecuencias = np.fft.fftfreq(len(Ruido_intento))
# Calcular el valor medio
valor_medio = np.mean(Ruido_intento)

# Calcular la PSD utilizando FFT
psd = np.abs(np.fft.fft(Ruido_intento))**2 / len(Ruido_intento)

# Calcular la función de autocorrelación
autocorrelacion = np.correlate(Ruido_intento, Ruido_intento, mode='full')

# Calcular la varianza
varianza = np.var(Ruido_intento)

# Imprimir resultados
print("Valor Medio:", valor_medio)
print("Varianza:", varianza)

plt.figure(figsize=(15,7))


time, voltaje = datos[0]
plt.subplot(2, 4, 1)
plt.plot(time,voltaje)
plt.grid()
plt.title("Ruido-CH1")
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')

time, voltaje = datos[1]
plt.subplot(2, 4, 2)
plt.plot(time,voltaje)
plt.grid()
plt.title("Señal+Ruido")
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')


plt.subplot(2, 4, 3)
plt.plot(tiempo,onda)
plt.grid()
plt.title("Señal Cuadrada")
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')

plt.subplot(2, 4, 4)
plt.plot(tiempo,Ruido_intento)
plt.grid()
plt.title("Señal Ruidosa sin señal cuadrada")
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')

plt.subplot(2, 4, 5)
plt.plot(Ruido_intento)
plt.grid()
plt.title('Muestras de Ruido Blanco')
plt.xlabel('Muestra')
plt.ylabel('Amplitud')

plt.subplot(2, 4, 6)
plt.plot(frecuencias, psd)
plt.grid()
plt.title('Densidad Espectral de Potencia')
plt.xlabel('Frecuencia')
plt.ylabel('PSD')

plt.subplot(2, 4, 7)
plt.plot(autocorrelacion)
plt.grid()
plt.title('Autocorrelación')
plt.xlabel('Desplazamiento')
plt.ylabel('Valor')

plt.tight_layout(pad=2.0)  # Ajustar espaciado con un valor de padding
plt.show()