# rompemuros.py
""" 
  Juego rompemuros
"""

from random import uniform 
from figuras import *
from pygame import Color
import sys
import pygame

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
NARANJA = (255, 126, 0)
AZUL = (0, 255, 255),
AMARILLO = (255, 255, 0)

D = 600
COLOR_FONDO = BLANCO
ESCALA = 10

# Dimensión X de la ventana (en pixels)
DIMX = 460
# Dimensión Y de la ventana (en pixels)
DIMY = 610

DIM_VENTANA = (DIMX, DIMY)

def x_pygame (x : float) -> float:
  return DIMX * x / ESCALA

def y_pygame (y : float) -> float:
  return DIMY * (ESCALA - y) / ESCALA
  
# Altura de un ladrillo
BRICK_HEIGHT = x_pygame(0.20)

# Separación horizontal entre los ladrillos 
BRICK_SEP_H = x_pygame(0.08)

# Número de ladrillos por fila
BRICKS_IN_ROW = 10

# Anchura de un ladrillo
BRICK_WIDTH = DIMX / BRICKS_IN_ROW - BRICK_SEP_H

# Separación vertical entre los ladrillos     
BRICK_SEP_V = x_pygame(0.08)

# Distancia desde la paROJO superior hasta la fila superior de ladrillos
BRICK_Y_BOTTOM_OFFSET = y_pygame(8)
    
# Número de filas de ladrillos
BRICK_ROWS = 10

# Anchura de la paleta
WIDTH_OF_PADDLE = x_pygame(1.20)

# Altura de la paleta
HEIGHT_OF_PADDLE = x_pygame(0.20)

# Distancia desde la pared inferior hasta la parte inferior de la paleta
PADDLE_OFFSET = y_pygame(0.30)

# Radio de la bola en pixels 
BALL_RADIUS = x_pygame(0.2)
    
#Frames por segundo para la animación
FPS = 60 

# Número de turnos 
# NTURNS = 3

def pintar_rectangulo (ventana, r : Rectangulo, c : Color):
  """ 
  Pinta en el lienzo un Rectangulo r con Color c
  """
  setPenColor(c)
  filledRectangle(r.x, r.y, r.ancho, r.alto)
def pintar_circulo (ventana, c : Circulo, co : Color):
  """ 
  Pinta en el lienzo un Circulo c con Color co
  """
  # setPenColor(c)
  # filledRectangle(r.x, r.y, r.ancho, r.alto)  
  pygame.draw.circle(ventana, co, (c.x, c.y), c.radio)
  
def pintar_lista (ventana, l : list):
  """ 
  Pinta una lista de Ladrillo(s)
  """
  for i in l:
    pintar_rectangulo(ventana, i, 3)

def fila_creada (n : int, ladrillo : Ladrillo, sep : float) -> list:
  """
  PRE: n >= 0  
       (int, Ladrillo, float) -> list[Ladrillo]
  
  Genera una fila horizontal de n ladrillos como ladrillo 
  separados a distancia sep. 
  El vertice inferior izquierdo de la fila muro es el que tiene ladrillo.
  El color de la fila es el que tiene ladrillo.
  """
  x = ladrillo.x + sep
  y = ladrillo.y
  ancho = ladrillo.ancho
  alto = ladrillo.alto
  color = ladrillo.color
  res = []
  for k in range(n):
    ladri = Ladrillo(x, y, ancho, alto, color)
    # pintar(ladri)    
    res += [ladri]
    x += ancho + sep
  return res  
    
def color (n : int) -> Color:
  """
  PRE: n in {0..9}  
  
  POST: resultado:
        n in {0, 1} --> ROJO 
        n in {2, 3} --> NARANJA
        n in {4, 5} --> AMARILLO
        n in {6, 7} --> VERDE
        n in {8, 9} --> AZUL
  """
  if 0 <= n <= 1:
    return ROJO
  elif 2 <= n <= 3:    
    return NARANJA
  elif 4 <= n <= 5:    
    return AMARILLO
  elif 6 <= n <= 7:    
    return VERDE
  else:    
    return AZUL
    
def muro_creado (m : int, n : int, ladrillo : Ladrillo,\
                 sepH : float, sepV : float) -> list:
  """
  PRE: n >= 0  
       (int, int, Ladrillo, float, float) -> list[Ladrillo]
  Genera un muro de ladrillos con m filas y n Ladrillo(s) como ladrillo
  en cada fila, 
  separados horizontalmente a distancia sepH y con distintos colores 
  Las filas están separadas entre ellas a una distancia sepV
  El vertice inferior izquierdo del muro es el que tiene ladrillo.
  El color de cada fila es el que tiene el ladrillo primero de la fila.
  """
  a = []
  for i in range (m):
    for j in range (n):
      x = ladrillo.x + j * (ladrillo.ancho+sepH)
      y = ladrillo.y + i * (ladrillo.alto + sepV)
      n_ladrillo = Ladrillo (x, y, ladrillo.ancho, ladrillo.alto, ladrillo.color)
      a.append(n_ladrillo)
  return a
    
      
  # colores = [ROJO, NARANJA, AMARILLO, VERDE, AZUL]

ladrillo = Ladrillo(0, 0, 50, 20, Color(0))

# Generar un muro de 3 filas y 5 columnas
muro = muro_creado(3, 5, ladrillo, 10, 15)

# Imprimir las posiciones de los ladrillos

