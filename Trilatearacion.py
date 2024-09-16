from geopy.distance import great_circle
from scipy.optimize import minimize
import numpy as np

def trilateracion(latlon1, r1, latlon2, r2, latlon3, r3):
    def distance(p1, p2):
        return great_circle(p1, p2).meters

    def objective(x):
        lat, lon = x
        p1 = (latlon1[0], latlon1[1])
        p2 = (latlon2[0], latlon2[1])
        p3 = (latlon3[0], latlon3[1])
        return (distance((lat, lon), p1) - r1)**2 + (distance((lat, lon), p2) - r2)**2 + (distance((lat, lon), p3) - r3)**2

    # Usar un punto medio aproximado como inicialización
    lat_init = (latlon1[0] + latlon2[0] + latlon3[0]) / 3
    lon_init = (latlon1[1] + latlon2[1] + latlon3[1]) / 3

    result = minimize(objective, (lat_init, lon_init), bounds=[(-90, 90), (-180, 180)])
    
    lat, lon = result.x
    return round(lat, 6), round(lon, 6)

# Ejemplo de uso
latlon1 = (-16.376086, -71.521743)
latlon2 = (-14.659863, -61.745231)
latlon3 = (-21.936406, -60.292095)
r1 = 901100
r2 = 374200
r3 = 557100

# Obtener el punto de intersección en latitud y longitud
interseccion_latlon = trilateracion(latlon1, r1, latlon2, r2, latlon3, r3)
print("Punto de intersección en Latitud y Longitud:", interseccion_latlon)