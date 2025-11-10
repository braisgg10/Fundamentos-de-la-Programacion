# rompemuros_test.py

from figuras import *
from pygame import Color
import pygame
from pygame.locals import QUIT
from rompemuros import *
from random import uniform

def inicializar_juego ():
  global ventana, fin, reloj 
  # Inicializar pygame
  pygame.init()
  # La ventana gráfica
  ventana = pygame.display.set_mode(DIM_VENTANA)
  # Poner el título en la ventana
  pygame.display.set_caption("rompemuros")
  # Variable de control del fin del juego
  fin = False
  # Reloj para velocidad de refresco de la ventana
  reloj = pygame.time.Clock()
  
def poner_ladrillos ():  
  global fin
  inicializar_juego()
  muro = muro_creado(BRICK_ROWS, BRICKS_IN_ROW, \
                   Ladrillo(0, BRICK_Y_BOTTOM_OFFSET, \
                            BRICK_WIDTH, BRICK_HEIGHT, NARANJA),\
                   BRICK_SEP_H, BRICK_SEP_V)
  while not fin:
    for event in pygame.event.get():
      if event.type == QUIT:
        fin = True
    ventana.fill(BLANCO)
    pintar_lista(ventana, muro)    
    pygame.display.flip()    
    reloj.tick(FPS)
  pygame.quit()
  
def poner_paleta ():  
  global fin
  inicializar_juego()
  paleta = Paleta(ESCALA/10, PADDLE_OFFSET,\
                  WIDTH_OF_PADDLE, HEIGHT_OF_PADDLE, NEGRO)
  while not fin:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:  paleta.mover(-20, x_pygame(ESCALA))
        if event.key == pygame.K_RIGHT: paleta.mover(20, x_pygame(ESCALA))
      if event.type == pygame.KEYUP: 
        if event.key == pygame.K_LEFT:  paleta.mover(-20, x_pygame(ESCALA))
        if event.key == pygame.K_RIGHT: paleta.mover(20, x_pygame(ESCALA))
      if event.type == QUIT: fin = True    
    ventana.fill(BLANCO)
    pintar_rectangulo(ventana, paleta, paleta.color)     
    pygame.display.flip()
    reloj.tick(FPS)
  pygame.quit()

def poner_ladrillos_y_paleta ():  
  pass

def poner_bola ():  
  global fin
  inicializar_juego()
 
  # Bola
  bola = Bola(0, DIMY-BRICK_Y_BOTTOM_OFFSET, BALL_RADIUS, \
              uniform(2, 4), uniform(2, 4), VERDE)

  while not fin:
    for event in pygame.event.get():
      if event.type == QUIT: fin = True    
    ventana.fill(BLANCO)
    pintar_circulo(ventana, bola, bola.color)     
    bola.mover(x_pygame(ESCALA), x_pygame(ESCALA) + (DIMY - DIMX))
    pygame.display.flip()
    reloj.tick(FPS)
  pygame.quit()
  
def poner_bola_y_paleta ():  
  pass  

def fijar_ladrillos ():
  """
  Toma dos parámetros del input en sys.argv[1] y sys.argv[2]
  Almacena el primer int en BRICKS_IN_ROW, 
  almacena el segundo int en BRICK_ROWS,
  y vuelve a calcular BRICK_WIDTH utilizando la fórmula dada en su declaración. 
  """
  global BRICKS_IN_ROW
  global BRICK_ROWS
  global BRICK_WIDTH 
  BRICKS_IN_ROW = int(sys.argv[1])
  BRICK_ROWS = int(sys.argv[2])
  BRICK_WIDTH = DIMX / BRICKS_IN_ROW - BRICK_SEP_H

def golpear_muro (bola : Bola, muro : list):
  """
  PRE: (Bola, list[Ladrillo])
  
  Rebota la bola al tocar el muro y borra el ladrillo correspondiente
  """
  pass
  
def poner_bola_paleta_y_muro ():  
  pass

# -- PRUEBAS  
# poner_ladrillos()    
# poner_paleta()
# poner_bola()
# poner_ladrillos_y_paleta()  
# poner_bola_y_paleta()

# fijar_ladrillos()  
# poner_bola_paleta_y_muro()  

