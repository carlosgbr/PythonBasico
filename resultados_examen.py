""" Funciones y condicionales if: resultados_examen.py
 Se ilustra el uso de funciones y la estructura if en Python
 Por https://about.me/carlosgbr
 Fecha: 02/01/2025
 Versión 1
 Actualizado: 02/01/2025
 Para Python 3.11 y superior
"""
def resultados_examen(puntuacion):
	if puntuacion > 95:
		grado = "Puntaje superior"
	elif puntuacion >=60:
		grado = "Aprobado"
	else:
		grado = "Reprobado"
	return grado
print(resultados_examen(65)) # Debe ser Aprobado
print(resultados_examen(55)) # Debe ser Reprobado
print(resultados_examen(60)) # Debe ser Aprobado
print(resultados_examen(95)) # Debe ser Aprobado
print(resultados_examen(100)) # Debe ser Puntaje superior
print(resultados_examen(0)) # Debe ser Reprobado
