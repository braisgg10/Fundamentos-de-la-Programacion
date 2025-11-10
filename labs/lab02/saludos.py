"""Libreria de funciones que producen saludos"""

import random

def hola_multi (nombre : str, num : int) -> str:
  """Da un string de la forma: "hola " repetido <num> veces, 
     seguido por <nombre>, seguido de "!". """    
  return "hola " * num + nombre + "!"

def hola_random (nombre : str) -> str:
  """VER ENUNCIADO"""
  reps = random.randint(1,6)
  return hola_multi(nombre, reps)
  
