""" Funciones: ordena_numeros.py
 Se ilustra el uso de funciones en Python
 Por https://about.me/carlosgbr
 Fecha: 02/01/2025
 Versión 1
 Actualizado: 02/01/2025
 Para Python 3.11 y superior
"""
# Esta función compara dos números y los devuelve
# en orden creciente.
def ordena_numeros(numero1, numero2):
	if numero2 > numero1:
		return numero1, numero2
	else:
		return numero2, numero1
# 1) Complete los espacios en blanco para que la declaración de impresión
# muestre el resultado de la llamada a la función
menor, mayor = ordena_numeros(100, 99)
print(menor, mayor)
