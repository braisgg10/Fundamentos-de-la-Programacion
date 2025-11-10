# punto_ops.py

"""
  Operaciones con Punto
"""
  
from stddraw import *
from color import Color
from random import uniform, normalvariate
from punto import Punto

D = 800
COLOR_FONDO = WHITE
ESCALA = 5
  
def iniciar_graficos (): 
  setCanvasSize(D, D)
  setXscale(-ESCALA, ESCALA)
  setYscale(-ESCALA, ESCALA)
  setPenRadius(0.5)
  clear(COLOR_FONDO)

def pintar_punto (p : Punto, c : Color):
  """ 
  Pinta el Punto p en el lienzo en color c
  """
  setPenColor(c)
  point(p.x,p.y)
    
def punto_medio (p1 : Punto, p2 : Punto) -> Punto:
  """ 
  POST: resultado: el punto medio del segmento que 
                   conecta p1 y p2
  """
    return Punto((p1.x+p2.x)/2,(p1.y+p2.y)/2)
    
def simetrico (p : Punto) -> Punto:
  """ 
  POST: resultado: el Punto simétrico a p respecto al eje y = x
  """
    return Punto(p.y,p.x)
def pintar_rejilla (n : int):
  """
  Pinta una rejilla o cuadrícula de tamaño 2n, con 2n líneas horizontales y
  2n líneas verticales
  """
  for x in range(-n+1, n):
    line(x, -n, x, n)
  for y in range(-n+1, n):
    line(-n, y, n, y)

def punto_alea_rect (ii : Punto, sd : Punto) -> Punto:
  """ 
  PRE: ii < sd 
  
  POST:
    resultado: un punto aleatorio dentro del rectángulo cuyo punto inferior 
               izquierdo es ii y cuyo punto superior derecho es sd
  """
    return Punto(uniform(ii.x,sd.x),uniform(ii.y,sd.y))
def punto_alea () -> Punto:
  """ 
  POST:
    resultado: un punto aleatorio dentro del lienzo
  """
    punto_alea_rect(Punto(-5,-5),Punto(5,5))
def nube (n : int):
  """
  Muestra una nube de n puntos aleatorios en modo gráfico
  """
    for i in range(1, n+1):
      punto_alea()
    
def puntos_test ():
  """
    Pruebas de diversas operaciones sobre Punto
  """
  pintar_rejilla(ESCALA)
  
  # Crear y visualizar puntos:
  p = Punto(0, 0)
  pintar_punto(p, BLACK)
  p = Punto(1, 2)
  pintar_punto(p, RED)
  q = Punto(-2, -2)
  pintar_punto(q, BLUE)
  
  # Calcular la distancia entre ellos:
  d = p.distancia(q)
  setPenColor()
  text(1, 4, f"La distancia del rojo al azul es {d:4.2f}")
  
  # Calcular y visualizar el punto medio:
  m = punto_medio(p, q)
  pintar_punto(m, GREEN)
  
  # Simétrico del punto rojo:
  s = simetrico(p)
  pintar_punto(s, PINK)
  
  # Visualizar 10 puntos aleatorios:
  for k in range(10):
    p = punto_alea_rect(Punto(1, -2), Punto(3, 0))
    pintar_punto(p, MAGENTA)

 
iniciar_graficos()   
#puntos_test()   
#nube(200)
show()
  

