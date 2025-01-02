""" Loops: loops_digitos.py
 Se ilustra el uso de funciones y la estructura if en Python.
 Por https://about.me/carlosgbr
 Fecha: 02/01/2025
 Versión 1
 Actualizado: 02/01/2025
 Para Python 3.11 y superior
"""
"""
ENUNCIADO: Complete la función digitos(n) que devuelve cuántos dígitos
tiene el número. Por ejemplo: 25 tiene 2 dígitos y 144 tiene 3 dígitos.
Consejo: puede calcular los dígitos de un número dividiéndolo por 10
una vez por dígito hasta que no queden dígitos.
"""
def digitos(n):
	cotador = 0
	if n == 0:
	    cotador = 1
	else:
	    cotador = 1
	    while (n >= 10):
	        cotador += 1
	        n = n//10
	        #imprime(n)
	return cotador
print(digitos(25))   # Debe imprimir 2
print(digitos(144))  # Debe imprimir 3
print(digitos(1000)) # Debe imprimir 4
print(digitos(0))    # Debe imprimir 1
