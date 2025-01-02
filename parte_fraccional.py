""" Funciones y condicionales if: parte_fraccional.py
 Se ilustra el uso de funciones y la estructura if en Python
 Por https://about.me/carlosgbr
 Fecha: 02/01/2025
 Versión 1
 Actualizado: 02/01/2025
 Para Python 3.11 y superior
"""
def parte_fraccional(numerador, denominador):
    if denominador == 0:
        resultado = 0
    else:
        resultado = (numerador // denominador) - numerador / denominador
        resultado = abs(resultado)
    return resultado
print(parte_fraccional(5, 5)) # Debe ser 0
print(parte_fraccional(5, 4)) # Debe ser 0.25
print(parte_fraccional(5, 3)) # Debe ser 0.66...
print(parte_fraccional(5, 2)) # Debe ser 0.5
print(parte_fraccional(5, 0)) # Debe ser 0
print(parte_fraccional(0, 5)) # Debe ser 0
