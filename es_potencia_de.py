""" Funciones y condicionales if: es_potencia_de.py
   Verificamos si un número es potencia de un número base dado. Utilizando una
   función Recursiva
 Por https://about.me/carlosgbr
 Fecha: 02/01/2025
 Versión 1
 Actualizado: 02/01/2025
 Para Python 3.11 y superior
"""
"""
ENUNCIADO: Completa los espacios en blanco para que la función es_potencia_de
devuelva si el número es una potencia de la base dada.
Nota: se supone que base es un número positivo.
Consejo: para funciones que devuelven un valor booleano,
puede devolver el resultado de una comparación.
"""
def es_potencia_de(numero, base):
  # Caso base: Cuando el número es menor que la base.
  if numero < base:
    # Si numero es igual a 1, este es una potencia (base**0).
    return False
  elif (base**3/numero) == 1:
      return True
  else:
      return False
  # Caso de Recursividad: Mantener dividiendo number por la base.
  return es_potencia_de(numero,base)
print(es_potencia_de(8,2)) # Debe ser True
print(es_potencia_de(64,4)) # Debe ser True
print(es_potencia_de(70,10)) # Debe ser False
