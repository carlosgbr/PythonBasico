""" Funciones y condicionales while: sum_divisores.py
 Se ilustra el uso de funciones y la estructura while en Python
 Por https://about.me/carlosgbr
 Fecha: 02/01/2025
 Versión 1
 Actualizado: 02/01/2025
 Para Python 3.11 y superior
"""
def sum_divisores(n):
  sum = 0
  divisor = n
  while divisor > 1:
    divisor = divisor - 1
    if (n % divisor) == 0:
        sum += divisor
  # Devuelve la suma de todos los divisores de n, sin incluir n
  return sum
print(sum_divisores(0))
# 0
print(sum_divisores(3)) # Debe ser sum de 1
# 1
print(sum_divisores(36)) # Debe ser sum de 1+2+3+4+6+9+12+18
# 55
print(sum_divisores(102)) # Debe ser be sum de 2+3+6+17+34+51
# 114
