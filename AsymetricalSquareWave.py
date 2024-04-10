import numpy as np
import matplotlib.pyplot as plt

def generar_onda_cuadrada_asimetrica(frecuencia, duracion_pulso, duracion_total):
    tiempo = np.linspace(-duracion_total, duracion_total, num=1000)
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

def main():
    frecuencia = 22  # Hz
    duracion_pulso = 0.015  # segundos
    duracion_total = 0.06  # segundos

    tiempo, onda = generar_onda_cuadrada_asimetrica(frecuencia, duracion_pulso, duracion_total)

    plt.plot(tiempo, onda)
    plt.title('Onda Cuadrada Asimétrica')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (V)')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
