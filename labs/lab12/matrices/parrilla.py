"""
 Parrilla gráfica apoyada en lista 2D usando pygame
 
 Ejemplo adaptado por el profesor Javier Galve (ETSIInf UPM) a partir del 
 programa  original del profesor Paul Vincent Craven (Simpson College Computer 
 Science,  Iowa, EEUU)
 Sample Python/Pygame Programs
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""

import pygame
from matrices import *

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# -- Constantes del juego --

# Ancho y alto de cada cuadro de la parrilla
DIMX_CUAD = 40
DIMY_CUAD = 40
# Dimensión de la parrilla 
DIM_PARRILLA = 10 
# Espacio entre cuadros
MARGEN = 5
# Dimensiones de la ventana gráfica
DIM_VENTANA = [(DIMX_CUAD+MARGEN)*DIM_PARRILLA, (DIMY_CUAD+MARGEN)*DIM_PARRILLA]
 
def inicializar_juego ():
  global parrilla, ventana, fin, reloj 
  # Crear la parrilla como una lista de int(s): 0 = BLANCO, 1 = VERDE
  parrilla = crea_2D(DIM_PARRILLA, DIM_PARRILLA, 0)
  # Inicializar pygame
  pygame.init()
  # La ventana gráfica
  ventana = pygame.display.set_mode(DIM_VENTANA)
  # Poner el título en la ventana
  pygame.display.set_caption("Parrilla con lista 2D")
  # Variable de control del fin del juego
  fin = False
  # Reloj para velocidad de refresco de la ventana
  reloj = pygame.time.Clock()

def atender_eventos ():
  """
  Atiende los eventos de teclado y/o ratón y actúa en consecuencia
  """
  global fin, parrilla
  for event in pygame.event.get():  
    if event.type == pygame.QUIT:  
      fin = True  
    elif event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      col = pos[0] // (DIMX_CUAD + MARGEN)
      fil = pos[1] // (DIMY_CUAD + MARGEN)
      parrilla[fil][col] = 1
      print("Click ", pos, "coords. de la parrilla: ", fil, col)
  
def dibujar_parrilla (parrilla : list):
  """
  PRE: list(int), 
       e in parrilla, e in {0, 1}, 0 = BLANCO, 1 = VERDE
  
  Dibuja la parrilla en BLANCO o en VERDE (ver la PRE)
  """
  for i in range(len(parrilla)):
    for j in range(len(parrilla[0])):
      color = BLANCO
      if parrilla[i][j] == 1: color = VERDE
      pygame.draw.rect(ventana, color, 
                       [(MARGEN + DIMX_CUAD) * j + MARGEN,
                       (MARGEN + DIMY_CUAD) * i + MARGEN, DIMX_CUAD, DIMY_CUAD])

# Bucle del juego                       
inicializar_juego()                     
while not fin:
  atender_eventos()
  ventana.fill(NEGRO)
  dibujar_parrilla(parrilla)
  pygame.display.flip()
  reloj.tick(60)
quit()