# palabra_secreta.py

"""
  Módulo con una clase: PalabraSecreta
"""

import random

class PalabraSecreta:
  """
  Palabra que debe adivinar un usuario en un juego del ahorcado.

  Atributos:
    palabra_secreta: la palabra a acertar (str de minúsculas)
    palabra_visible: palabra tal y como la ve el usuario: las letras de 
      palabra_secreta muestran las letras ya acertadas (str de minúsculas 
      y '_')
    palabra_secreta y palabra_visible tienen la misma longitud
  """

  def __init__(self):
    """
    resultado: Crea la palabra_secreta y la palabra_visible
               La palabra secreta es una palabra elegida al azar de la 
               lista_de_palabras
               La lista_de_palabras es creada a partir de un fichero de texto
               de nombre "palabras.txt"
    """
    lista_de_palabras = PalabraSecreta.carga_palabras("palabras.txt")
    # print(lista_de_palabras)
    posicion_azar = random.randint(0, len(lista_de_palabras)-1)
    self.palabra_secreta = lista_de_palabras[posicion_azar]
    self.palabra_visible = len(self.palabra_secreta)*'_' 

  def mostrar_palabra_visible (self):
    """
    Muestra la palabra acertada hasta ahora
    """
    print ("Tu intento : " + self.palabra_visible)
 
  def mostrar_palabra_secreta (self):
    """
    Muestra la palabra que había que acertar  
    """
    print ("La palabra a acertar era: " + self.palabra_secreta)

  def hay_aciertos (self, car : str) -> bool:
    """
    PRE:
      len(car) = 1
    POST:
      resultado: existe al menos un caracter en palabra_secreta igual a car
    EJEMPLOS:
      hay_aciertos("o", "opaco") --> True
      hay_aciertos("o", "opaca") --> True
      hay_aciertos("o", "pac") --> False
    """
    for i in self.palabra_secreta:
        if i==car:
            return True
    return False
    
  def cambiar (self, car : str):
    """
    PRE:
      len(car) = 1

    Cambia la palabra_visible por las apariciones de car en palabra_secreta
    """
    lista=list(self.palabra_visible)
    w=""
    p=0
    for i in self.palabra_secreta:
        if i==car:
            w=w+car
            p+=1
        else:
            w=w+lista[p]
            p+=1
    self.palabra_visible= w
    return self.palabra_visible
    
  def esta_acertada (self) -> bool:
    """
    POST:
      resultado: la palabra secreta coincide con la visible
    """
    return self.palabra_secreta==self.palabra_visible
    
  def carga_palabras (nombre_fichero : str) -> list:
    """
    POST:
      resultado: una lista de palabras leídas de un fichero llamado nombre_fichero
                 sin saltos de línea al final de cada palabra 
    """
    salida = ""
    lineas = (linea for linea in open(nombre_fichero, 'r'))
    for linea in lineas:
        salida=salida+linea
    return salida.split()
    
  def limpias (palabras : list) -> list:
    """
    POST:
      resultado: una lista de palabras sin saltos de línea al final
    """
    lista=[]
    for palabra in palabras:
        lista.append(palabra.strip())
    return lista  