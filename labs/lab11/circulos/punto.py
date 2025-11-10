# punto.py
""" 
  Contiene una clase Punto que permite
  manejar puntos en el plano.
"""

from math import sqrt

class Punto:
  """
  Punto del espacio 2D
    
    x : float -- coordenada x
    y : float -- coordenada y
  """

  def __init__ (self, x : float, y : float):
    """ 
    Constructor de un Punto
    """
    self.x = x
    self.y = y

  def __str__ (self) -> str:
    """ 
    POST: 
      resultado: Punto como texto
      
    Para aplicar esta función a un Punto p, escribir print(p)
    """
    return "(" + str(self.x) + ", " + str(self.y) + ")"
    
  def __eq__ (self, otro) -> bool:
    """ 
    PRE: otro : Punto
    
    POST: resultado: self es igual (por contenido) a otro 
    """
    return self.x == otro.x and self.y == otro.y
    
  def distancia (self, otro) -> float:
    """ 
    PRE: otro : Punto
    
    POST: resultado: Calcula la distancia de self a otro
    """
    return sqrt((self.x - otro.x)**2 + (self.y - otro.y)**2)
    
