# reloj_digital.py

"""
  Pequeñas aplicaciones de la clase Hora
"""
  
from hora import Hora
from stddraw import *
from color import Color
from fecha import Fecha

DIM = 5 
TAM_FUENTE = 48
COLOR_FONDO = GRAY
setXscale(-DIM, DIM)
setYscale(-DIM, DIM)
setFontFamily("Helvetica")
setFontSize(TAM_FUENTE)

def reloj ():
  """ 
  Muestra un reloj con formato: "hh:mm:ss" incrementándose instante a instante.
  Cada instante es un segundo.
  Empieza en la hora actual.
    hh -- horas
    mm -- minutos
    ss -- segundos
  """
  while True:
    clear(COLOR_FONDO)
    text(0, 0, str(Hora.ahora()))
    show(1000)

def cronometro ():
  """ 
  Muestra un cronómetro con el tiempo en formato: "mm:ss:cc" incrementándose 
  instante a instante.
  Cada instante es una centésima de segundo.
  Empieza en 00:00:00
    mm -- minutos
    ss -- segundos
    cc -- centésimas de segundo    
  """
  h = Hora(0, 0, 0)
  while True:
    clear(COLOR_FONDO)
    text(0, 0, str(h))
    show(100)
    h = h + Hora(0, 0, 1)
  
def temporizador (inicial : Hora):
  """ 
  Muestra un temporizador con formato: "hh:mm:ss" decrementándose instante a 
  instante.
  Cada instante es un segundo.
  Empieza en la hora inicial.
    hh -- horas
    mm -- minutos
    ss -- segundos
  """
  activo = True
  h = inicial
  while activo == True:
      clear(COLOR_FONDO)
      text(0, 0, str(h))
      show(600)
      h = h - Hora(0, 0, 1)
      if h == Hora(0,0,0): #Para que el temporizador no de horas negativas
          activo = False
  
def alarma (h : Hora):
  """ 
  h es la hora programada para la alarma.
  Muestra un reloj con formato: "hh:mm:ss" incrementándose instante a instante.
  Cada instante es un segundo.
  Muestra la hora h de la alarma con el texto: "alarma: h"
  Muestra un mensaje "¡¡ALARMA!!" cuando la hora actual llegue a la hora h, 
  pero el reloj sigue.
  Empieza en la hora actual.
    hh -- horas
    mm -- minutos
    ss -- segundos
  """
  ahora=Hora.ahora()
  while not ahora.__eq__(h):
      ahora=Hora.ahora()
      clear(COLOR_FONDO)
      text(0, 0, str(ahora))
      show(600)
  clear(COLOR_FONDO)
  text(0,0,str("¡¡ALARMA!!"))
  show()

def reloj_calendario ():
  """ 
  = NECESARIA LA CLASE Fecha =

  Muestra un reloj con formato: "hh:mm:ss" incrementándose instante a instante.
  Muestra también la fecha de hoy en la parte de abajo con un tipo de letra 
  más pequeño que el reloj.
  Cada instante es un segundo.
  Empieza en la hora actual.
    hh -- horas
    mm -- minutos
    ss -- segundos
  """
  while True:
    clear(COLOR_FONDO)
    text(0,1, str(Hora.ahora()))
    text(0,-1,str(Fecha.hoy()))
    show(1000)

def calendario_acelerado ():
  """ 
  = NECESARIA LA CLASE Fecha =
  
  Muestra la fecha con formato: "dd:mm:aa" incrementándose instante 
  a instante.
  Cada instante es un segundo.
  Empieza en la fecha de hoy.
    dd -- día
    mm -- mes
    aa -- año
  """
  h = Fecha.hoy()
  while True:
    clear(COLOR_FONDO)
    text(0, 0, str(h))
    show(1000)
    h = Fecha.siguiente(h)
    
# reloj()
# cronometro()
#temporizador(Hora(0, 0, 5))
#alarma(Hora.ahora() + Hora(0, 0, 5))
#reloj_calendario()
calendario_acelerado()