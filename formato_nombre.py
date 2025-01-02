""" Funciones y condicionales if: formato_nombre.py
 Se ilustra el uso de funciones y la estructura if en Python.
 Por https://about.me/carlosgbr
 Fecha: 02/01/2025
 Versión 1
 Actualizado: 02/01/2025
 Para Python 3.11 y superior
"""

def formato_nombre(primer_nombre, apellido):
    """
    Función que genera un formato específico para nombres completos.
    
    Argumentos:
    - primer_nombre: Primer nombre de la persona (string).
    - apellido: Apellido de la persona (string).
    
    Retorna:
    - Una cadena de texto con el formato adecuado, dependiendo de los argumentos recibidos.
    """
    # Verifica si ambos valores no están vacíos
    if (primer_nombre != "") and (apellido != ""):
        # Si ambos están presentes, devuelve "Apellido, Primer Nombre"
        Nombre = "Nombre: " + apellido + ", " + primer_nombre
    else:
        # Si alguno de los valores está vacío, maneja los casos específicos
        if (primer_nombre == "") and (apellido == ""):
            # Si ambos están vacíos, devuelve una cadena vacía
            Nombre = ""
        elif primer_nombre != "":
            # Si solo está presente el primer nombre, devuelve solo ese nombre
            Nombre = "Nombre: " + primer_nombre
        elif apellido != "":
            # Si solo está presente el apellido, devuelve solo ese apellido
            Nombre = "Nombre: " + apellido
    return Nombre  # Retorna el formato generado

# Pruebas para verificar el funcionamiento de la función
print(formato_nombre("Paulina", "Angel"))
# Debería ser "Nombre: Angel, Paulina"

print(formato_nombre("", "Stephanie"))
# Debería ser "Nombre: Stephanie"

print(formato_nombre("Brozo", ""))
# Debería ser "Nombre: Brozo"

print(formato_nombre("", ""))
# Debería ser ""
