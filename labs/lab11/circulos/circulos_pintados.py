# circulos_pintados.py
# Galve
""" 
  Módulo para pintar los objetos de la clase Circulo 
  generados aleatoriamente que son exteriores entre sí.
"""

from random import uniform 
from circulo import *
from circulo_ops import *
from stddraw import *
from color import Color

D = 800
COLOR_FONDO = BLACK
ESCALA = 10

def iniciar_graficos (): 
  setCanvasSize(D, D)
  setXscale(-ESCALA, ESCALA)
  setYscale(-ESCALA, ESCALA)
  setPenRadius(0.001)
  clear(COLOR_FONDO)

def es_exterior_a_todos (c : Circulo, l : list):
  """ 
  POST: resultado: c es exterior a todos los Circulo(s) de l
  """
  for otro in l:
      if son_secantes(c, otro):  # Comprueba si los círculos se solapan
          return False
  return True      
    
def circulo_alea (n : int):
  """ 
  Genera un Circulo de radio 1 cuyo centro es ubicado 
  aleatoriamente dentro de un cuadrado de 2n x 2n 
  centrado en (0,0). 
  """
  x = uniform(-n,n)
  y = uniform(-n,n)
  centro = Punto(x,y)
  radio = 1
  return Circulo(centro, radio)

def pintar_circulos_aleatorios (m:int, n:int):
  iniciar_graficos()
  for i in range (m):
    pintar_circulo(circulo_alea(n), MAGENTA)
  show()
  
def genera (m : int, n : int) -> list:
  """ 
  PRE: m >= 0, n >= 0
  POST: resultado: una lista formada por m Circulos de radio 1 cuyo centro 
        está ubicado aleatoriamente dentro de un cuadrado de 2n x 2n centrado 
        en (0,0)
  """
  lista = []
  for i in range (m):
      i = circulo_alea(n)
      lista.append (i)
  return lista

def genera_exteriores (m : int, n : int) -> list:
  """ 
  PRE: m >= 0, n >= 0
  POST: resultado: una lista formada por m Circulos de radio 1 cuyo centro 
                   está ubicado aleatoriamente dentro de un cuadrado de 2n x 2n 
                   centrado en (0,0) y que son todos exteriores mutuamente entre 
                   si
  """
  lista=[]
  i=0
  MAX_INTENTOS = 1000
  while len(lista) < m and i < MAX_INTENTOS:
    c = circulo_alea(n)
    if es_exterior_a_todos(c, lista):
      lista += [c]
    i+=1  
  if i >= MAX_INTENTOS:
        print("No se pudieron generar suficientes círculos.")
  return lista
            
    
def main ():
  iniciar_graficos()
  m = 100
  # lista = genera(m, ESCALA)
  lista = genera_exteriores(m, ESCALA)
  pintar_circulos(lista, MAGENTA)
  # Estadísticas:
  #num_visualizados = len(lista)
  #ratio = (num_visualizados // m) * 100
  #print(f"m = {m:3d} num_visualizados = {num_visualizados:3d} \
  #ratio = {ratio:5.2f}%")
  show()

if __name__ == '__main__':
  main()    


