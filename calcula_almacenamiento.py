""" Funciones y condicionales: calcula_almacenamiento.py
  Se ilustra el uso de funciones y la estructura if en Python
 Por https://about.me/carlosgbr
 Fecha: 02/01/2025
 Versión 1
 Actualizado: 02/01/2025
 Para Python 3.11 y superior
"""
def calcula_almacenamiento(tamanoarchivo):
    tamano_bloque = 4096
    # Use la división de piso para calcular cuántos bloques están completamente ocupados
    bloques_completos = tamanoarchivo // tamano_bloque
    # Use el operador de módulo para verificar si hay algún resto
    residuo_parcial_bloque = tamanoarchivo % tamano_bloque
    # Dependiendo de si hay un resto o no, devuelva el número correcto.
    if residuo_parcial_bloque > 0:
        return bloques_completos * tamano_bloque + tamano_bloque
    return bloques_completos * tamano_bloque
print(calcula_almacenamiento(1))    # Debiera ser 4096
print(calcula_almacenamiento(4096)) # Debiera ser 4096
print(calcula_almacenamiento(4097)) # Debiera ser 8192
print(calcula_almacenamiento(6000)) # Debiera ser 8192
