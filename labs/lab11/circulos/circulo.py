# circulo.py

""" 
  Contiene una clase que representa círculos en el plano.
"""

from punto import *

class Circulo:
  """
    centro : Punto -- el centro del círculo
    radio : float  -- el radio del círculo, radio >= 0
    """
  def __init__ (self, p : Punto, r : float):
    """ 
    PRE: r >= 0
    Crea un objeto de tipo Circulo con 
    centro p y radio r.
    """
    self.centro = p
    self.radio = r
    
  def __str__(self) -> str:
    """ 
    Visualizador de un Circulo en modo texto.    
    """
    return f" Las coordenadas de tu punto son: ({self.centro.x}, {self.centro.y}) y su radio es: {self.radio}"

  def __eq__ (self, otro) -> bool:
    """ 
    PRE: otro : Circulo
    POST: resultado: self == otro
    """
    return self.centro == otro.centro and self.radio == otro.radio

  def distancia (self, otro) -> float:
    """ 
    PRE: otro : Circulo
    POST: resultado: distancia de self a otro.
    """
    return self.centro.distancia(otro.centro)
