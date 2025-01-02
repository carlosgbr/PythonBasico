""" Funciones y condicionales while: imprimir_factores_primos.py
 Se ilustra el uso de funciones y la estructura while en Python
 Por https://about.me/carlosgbr
 Fecha: 02/01/2025
 Versión 1
 Actualizado: 02/01/2025
 Para Python 3.11 y superior
"""
def imprimir_factores_primos(numero):
    # Comience con dos, que es el primer primo
    factor = 2
    # Continúe hasta que el factor sea mayor que el número
    while factor <= numero:
    # Verificar si el factor es un divisor de número
        if not (numero % factor != 0):
        # Si es así, imprímalo y divida el número original
            print(factor)
            numero /= factor
        else:
        # Si no es así, incremente el factor en uno
            factor += 1
    return "Done"
imprimir_factores_primos(100)
# Debe imprimir 2,2,5,5
