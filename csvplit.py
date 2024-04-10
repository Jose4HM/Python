import pandas as pd

# Ruta al archivo CSV de entrada
archivo_entrada = "C:/Users/Nitro/Desktop/Universidad/samples911.csv"

# Cargar el archivo CSV en un DataFrame de pandas
data = pd.read_csv(archivo_entrada)

# Reducir a la mitad de las filas
mitad_filas = 1000000

# Tomar solo la mitad de los datos
data_reducida = data.head(mitad_filas)

# Ruta al archivo CSV de salida
archivo_salida = "C:/Users/Nitro/Desktop/Universidad/samples1e6.csv"

# Guardar el DataFrame reducido en un nuevo archivo CSV
data_reducida.to_csv(archivo_salida, index=False)

print(f"Se ha reducido el archivo a la mitad y guardado en {archivo_salida}.")
