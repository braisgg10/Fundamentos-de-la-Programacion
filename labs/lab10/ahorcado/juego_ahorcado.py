# juego_ahorcado.py

"""
  Juego del ahorcado versión OO
"""  

from palabra_secreta import PalabraSecreta
import ahorcado

MAX_FALLOS = 6 #Numero maximo de fallos permitido 
               #Se puede variar en funcion de como se dibuje el muñeco
               
def mostrar_fallos (fallos : int):
  """
  Muestra el numero de fallos hasta ahora
  """
  texto = "Llevas " + str(fallos) + " fallo"
  if fallos > 1:
    texto += "s" 
  print(texto)
  
def jugar ():
  juego = PalabraSecreta()
  n_fallos = 0
  fin = False
  while n_fallos < MAX_FALLOS and not fin:
    juego.mostrar_palabra_visible()
    intento = input("Teclea una letra: ")
    if juego.hay_aciertos(intento.lower()):
      juego.cambiar(intento.lower())
    else:
      n_fallos += 1
      mostrar_fallos(n_fallos)
      ahorcado.mostrar_estado(n_fallos)
    if juego.esta_acertada():
      print("ACERTADA!")
      fin = True
  juego.mostrar_palabra_secreta()

jugar()