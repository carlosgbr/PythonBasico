""" Funciones y condicionales if: palabra_mas_larga.py
 Se ilustra el uso de funciones y la estructura if en Python
 Por https://about.me/carlosgbr
 Fecha: 02/01/2025
 Versión 1
 Actualizado: 02/01/2025
 Para Python 3.11 y superior
"""
def palabra_mas_larga(palabra1, palabra2, palabra3):
	if len(palabra1) >= len(palabra2) and len(palabra1) >= len(palabra3):
		palabra = palabra1
	elif len(palabra2) >= len(palabra3):
		palabra = palabra2
	else:
		palabra = palabra3
	return(palabra)
print(palabra_mas_larga("silla", "sillón", "mesa"))
print(palabra_mas_larga("cama", "aro", "baúl"))
print(palabra_mas_larga("laptop", "notebook", "desktop"))
