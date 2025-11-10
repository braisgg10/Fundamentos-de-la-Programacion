import math
from math import sqrt

def creciente_hasta (n : int) -> str:
  """
  PRE: n in {0..9} 
  POST: resultado: un texto formado por los n primeros números concatenados
                   en orden creciente
  """
  a=""
  if n == 0:
    return a
  else:
      for i in range (1,n+1):
          a = a + i
      return a

def decreciente_hasta (n : int) -> str:
  """
  PRE: n in {1..9} 
  POST: resultado: un texto formado por los n primeros números concatenados
                   en orden decreciente
  """
  a=""
  if n == 0:
      return a
  else:
      for i in range (n,0):
          a = a + i
      return a

def crece_decrece_hasta (n : int) -> str:
  """
  PRE: n in {1..9} 
  POST: resultado: un texto formado por la concatenación de:
                   . los n-1 primeros números en orden creciente
                   . el número n
                   . los n-1 primeros números en orden decreciente
  """
  a=""
  b=""
  for i in range (1,n):
          a = a + i
  for j in range (n,0):
          b = b + j
  p = a + b  

    

def fermat_prop_fun (n : int) -> str:
  """
  PRE: n >=1 
  POST: resultado: un texto formado por n líneas
                   en cada línea muestra esta propiedad para un i, 
                   con i in {1..n}
  """
    
  p=""
  for i in range (n):
      p+= sqrt(crece_decrece_hasta(i)) + "\n"
  return p