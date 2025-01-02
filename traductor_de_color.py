""" Funciones y condicionales if: traductor_de_color.py
 Se ilustra el uso de funciones y la estructura if en Python
 Por https://about.me/carlosgbr
 Fecha: 02/01/2025
 Versión 1
 Actualizado: 02/01/2025
 Para Python 3.11 y superior
"""
def traductor_de_color(color):
	if color == "rojo":
		hex_color = "#ff0000"
	elif color == "verde":
		hex_color = "#00ff00"
	elif color == "azul":
		hex_color = "#0000ff"
	else:
		hex_color = "desconocido"
	return hex_color
print(traductor_de_color("azul")) # Debiera ser #0000ff
print(traductor_de_color("amarillo")) # Debiera ser desconocido
print(traductor_de_color("rojo")) # Debiera ser #ff0000
print(traductor_de_color("negro")) # Debiera ser desconocido
print(traductor_de_color("verde")) # Debiera ser #00ff00
print(traductor_de_color("rosa")) # Debiera ser desconocido
