"""Da una respuesta satisfactoria cuando el estudiante implementa hola_natural() correctamente en el modulo saludos"""

import saludos

print()  # imprime unas lineas en blanco para que la salida se vea mejor
print() 
nombre = input('Teclee su nombre: ')
output = "Hola " + nombre 
if output is not None and output.startswith("hola "):
  print(output)
  print("Enhorabuena, has completado tu primer programa ")
  print("de Fundamentos de la Programacion!")
else:
  print("Parece que te falta algo aun para acabar el lab.")
