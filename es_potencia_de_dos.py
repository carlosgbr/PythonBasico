""" Funciones y condicionales while:  es_potencia_de_dos.py
 Se ilustra el uso de funciones y la estructura while en Python
 Por https://about.me/carlosgbr
 Fecha: 17/04/2022
 Versión 1
 Actualizado: 02/01/2025
 Para Python 3.11 y superior
"""
def es_potencia_de_dos(n):  # Define una función para comprobar si un número es una potencia de dos
    if n <= 0:  # Comprueba si el número es menor o igual a 0
        return False  # Devuelve False, ya que las potencias de dos son números positivos

    # Divide repetidamente entre 2 mientras sea divisible por 2
    while n % 2 == 0:  # Itera mientras n sea divisible por 2
        n = n / 2  # Divide n entre 2

    # Si el resultado final es 1, es una potencia de dos
    return n == 1  # Devuelve True si n es 1, de lo contrario devuelve False
#Comprobación
print(es_potencia_de_dos(0)) # Debe ser False
print(es_potencia_de_dos(1)) # Debe ser True
print(es_potencia_de_dos(8)) # Debe ser True
print(es_potencia_de_dos(9)) # Debe ser False
