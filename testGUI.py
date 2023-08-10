import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo
x = np.random.rand(20)
y = np.random.rand(20)

fig, ax = plt.subplots()

# Crear el gráfico scatter
scatter = ax.scatter(x, y)

# Función para mostrar los valores al pasar el cursor sobre un punto
def mostrar_valores(event):
    if event.inaxes == ax:
        index = scatter.contains(event)[1]["ind"][0]
        x_val = x[index]
        y_val = y[index]
        ax.annotate(f'({x_val:.2f}, {y_val:.2f})', (x_val, y_val), textcoords="offset points", xytext=(0,10), ha='center')

# Conectar el evento de movimiento del cursor a la función
fig.canvas.mpl_connect("motion_notify_event", mostrar_valores)

plt.show()
