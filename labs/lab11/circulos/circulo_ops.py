# circulo_ops.py

""" 
  Operaciones con objetos de la clase Circulo.
"""

from circulo import *
from punto import *
from stddraw import *
from color import Color

D = 800
COLOR_FONDO = BLACK
ESCALA = 5

def iniciar_graficos (): 
  setCanvasSize(D, D)
  setXscale(-ESCALA, ESCALA)
  setYscale(-ESCALA, ESCALA)
  setPenRadius(0.01)
  clear(COLOR_FONDO)

def pintar_circulo (c : Circulo, color : Color):
  """ 
  Pinta en el lienzo un Circulo c con el Color color
  """
  xc = c.centro.x
  yc = c.centro.y
  r = c.radio
  setPenColor(color)
  filledCircle (xc, yc, r)
    
def pintar_circulos (l : list, color : Color):
  """ 
  PRE: l : list[Circulo]
  
  Pinta en el lienzo una lista de Circulo(s) l con el Color color
  """
  for c in l:
    pintar_circulo(c,color)
  show() 
def son_secantes (uno : Circulo, otro : Circulo) -> bool:
  """ 
  POST: resultado: uno y otro se cortan
  """
  return uno.centro.distancia(otro.centro) < (uno.radio + otro.radio)
    
def main ():

  # 1. Constructor:
  p00 = Punto(0.0, 0.0)
  p24 = Punto(2.0, 4.0)
  c00 = Circulo(p00, 1)
  c24 = Circulo(p24, 2)
  # 2. Visualizador:
  print("c00 = ", c00)
  print("c24 = ", c24)
  
  # Observador:
  print(f"c00.distancia(c24) = {c00.distancia(c24):5.2f}")

  # Comparador:
  print("c00 == Circulo(Punto(0, 0), 1) =>", c00 == Circulo(Punto(0, 0), 1))
  print("c00 is Circulo(Punto(0, 0), 1) =>", c00 is Circulo(Punto(0, 0), 1))
  
  # son_secantes:
  print("son_secantes(c00, c24) =", son_secantes(c00, c24))
   
  # Gráfico:
  # iniciar_graficos() 
  # pintar_circulo(c00, BLUE)
  # pintar_circulo(c24, RED)  
  # show()

  # Listas:
  # lista = [c00, c24, Circulo(Punto(-3, -3), 1)]
  # iniciar_graficos() 
  # pintar_circulos(lista, MAGENTA)
  # show()
  
if __name__ == '__main__':
  main()

# p00 = Punto(0.0, 0.0)
# p24 = Punto(2.0, 4.0)
# c00 = Circulo(p00, 1)
# c24 = Circulo(p24, 2)
# lista = [c00, c24, Circulo(Punto(-3, -3), 1)]
# iniciar_graficos() 
# pintar_circulos(lista, MAGENTA)
# show()
  
# show()

