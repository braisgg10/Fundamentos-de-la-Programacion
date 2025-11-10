"""
  Juego del ahorcado
"""  

import random
import ahorcado

MAX_FALLOS = 6 #Numero maximo de fallos permitido 
               #Se puede variar en funcion de como se dibuje el muñeco
               
def inicializado () -> (str, str):
    palabras = carga_palabras ("palabras.txt")
    palabras = [palabra for palabra in palabras if len(palabra) <= 10]
    if not palabras:
        raise ValueError("No hay palabras adecuadas en el archivo.")
    palabra_secreta = random.choice(palabras).lower()
    palabra_visible = "_" * len(palabra_secreta)
    return palabra_secreta, palabra_visible 
  
def carga_palabras (nombre_fichero : str) -> list:
  """
  POST:
    resultado: una lista de palabras leídas de un fichero llamado nombre_fichero
               sin saltos de línea al final de cada palabra 
  """
  with open(nombre_fichero, "r", encoding="utf-8") as file:
      return [palabra.strip() for line in file for palabra in line.split()]

  
def mostrar_palabra_visible (palabra : str):
  """
  Muestra la palabra acertada hasta ahora
  """
  print("Palabra  visible: " + " ".join(palabra))
  
def mostrar_palabra_secreta (palabra : str):
  """
  Muestra la palabra que había que acertar  
  """
  print("La palabra secreta era: " + palabra)

def hay_aciertos (car : str, referencia : str) -> bool:
  """
  PRE:
    len(car) = 1
  POST:
    resultado: existe al menos un caracter en referencia igual a car
  EJEMPLOS:
    hay_aciertos("o", "opaco") --> True
    hay_aciertos("o", "opaca") --> True
    hay_aciertos("o", "pac") --> False
  """
  return car in referencia
  
def cambiada (palabra : str, car : str, referencia : str) -> str:
    return "".join([car if referencia[i] == car else palabra[i] for i in range(len(referencia))])
  
def esta_acertada (secreta : str, visible : str) -> bool:
  """
  POST:
    resultado: la palabra secreta coincide con la visible
  """
  return secreta == visible

def mostrar_fallos (fallos : int):
  """
    Muestra el numero de fallos hasta ahora
  """
  print(f"\nNúmero de fallos: {fallos}")
  ahorcado.mostrar_estado(fallos)
  
def jugar ():
    palabra_secreta, palabra_visible = inicializado()
    n_fallos = 0
    fin = False
    while n_fallos < MAX_FALLOS and not fin:
        mostrar_palabra_visible(palabra_visible)
        intento = input("Teclea una letra: ").lower()
        if len(intento) != 1 or not intento.isalpha():
            print("Por favor, introduce una sola letra.")
            continue
        if hay_aciertos(intento, palabra_secreta):
            palabra_visible = cambiada(palabra_visible, intento, palabra_secreta)
        else:
            n_fallos += 1
            mostrar_fallos(n_fallos)
        if esta_acertada(palabra_secreta, palabra_visible):
            print("¡Has ganado!")
            fin = True
    if not fin:
        print("¡Has perdido!")
    mostrar_palabra_secreta(palabra_secreta)
 
jugar()