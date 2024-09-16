from geopy.distance import great_circle
from scipy.optimize import minimize
import numpy as np

def decimal_to_dms(degrees):
    d = int(degrees)
    minutes = int((degrees - d) * 60)
    seconds = (degrees - d - minutes / 60) * 3600
    return d, minutes, seconds

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
    lat = round(lat, 6)
    lon = round(lon, 6)

    # Convertir a formato DMS
    lat_dms = decimal_to_dms(abs(lat))
    lon_dms = decimal_to_dms(abs(lon))

    lat_hemisphere = "N" if lat >= 0 else "S"
    lon_hemisphere = "E" if lon >= 0 else "W"
    
    lat_dms_str = f"{lat_dms[0]}°{lat_dms[1]}'{lat_dms[2]:.1f}\"{lat_hemisphere}"
    lon_dms_str = f"{lon_dms[0]}°{lon_dms[1]}'{lon_dms[2]:.1f}\"{lon_hemisphere}"
    
    # Generar el enlace de Google Maps en formato DMS
    maps_url = f"https://www.google.com/maps/search/?api=1&query={lat_dms_str}+{lon_dms_str}"
    return lat, lon, maps_url

# Ejemplo de uso
latlon1 = (-16.376086, -71.521743)
latlon2 = (-14.659863, -61.745231)
latlon3 = (-21.936406, -60.292095)
r1 = 901100
r2 = 374200
r3 = 557100

# Obtener el punto de intersección en latitud y longitud
lat, lon, maps_url = trilateracion(latlon1, r1, latlon2, r2, latlon3, r3)
print(f"Punto de intersección en Latitud y Longitud: ({lat}, {lon})")
print(f"Enlace a Google Maps: {maps_url}")
