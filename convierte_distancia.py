""" Funciones: convierte_distancia.py
 Se ilustra el uso de funciones en Python
 Por https://about.me/carlosgbr
 Fecha: 02/01/2025
 Versión 1
 Actualizado: 02/01/2025
 Para Python 3.11 y superior
"""
# 1) Complete la función para devolver el resultado de la conversión.
def convierte_distancia(millas):
	km = millas * 1.6  # aproximadamente 1.6 km en 1 milla
	return km
mi_viaje_en_millas = 55
# 2) Convierta mi_viaje_en_millas a kilómetros llamando a la función anterior
mi_viaje_en_km = convierte_distancia(mi_viaje_en_millas)
# 3) Complete el espacio en blanco para imprimir el resultado de la conversión
print("La distancia en kilómetros es " + str(mi_viaje_en_km))
# 4) Calcule el viaje de ida y vuelta en kilómetros duplicando el resultado,
# y complete el espacio en blanco para imprimir el resultado
print("El viaje de ida y vuelta en kilómetros es " + str(mi_viaje_en_km * 2))
