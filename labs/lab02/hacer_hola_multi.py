"""
Un script que llama a saludos.hola_multi() 
con varios argumentos.
"""

import saludos

print(saludos.hola_multi("Wen", 2))
print(saludos.hola_multi("Paco", 3))
print(saludos.hola_multi("Polifemo", 1))
print(saludos.hola_multi(Wen, 2)) #No funciona porque Wen no es un string
