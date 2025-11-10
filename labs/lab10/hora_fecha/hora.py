# hora.py

""" 
  Contiene una clase Hora 
"""

from datetime import datetime

class Hora ():
  """
  Hora del reloj: tiempo transcurrido desde la media noche hasta el momento 
  actual, asumiendo que un día tiene 24*60*60 segundos.
    
    hh : int -- horas    -- hh in {0..23} 
    mm : int -- minutos  -- mm in {0..59}
    ss : int -- segundos -- ss in {0..59}
  """
  
  def __init__ (self, hh : int, mm : int, ss : int):
    """ 
    PRE: 
      Hora(int, int, int) -> Hora
      
    Constructor de una Hora
    """
    self.hh = hh;
    self.mm = mm;
    self.ss = ss;
 
  def __str__ (self) -> str:
    """ 
    PRE: 
      str() -> str
    POST: 
      resultado: Hora como texto      
    """
    return f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}"
    
  # @staticmethod  
  def ahora (): 
    """ 
    PRE: 
      ahora() -> Hora
    POST: 
      resultado: la Hora ahora
    """
    ahora = datetime.now()
    return Hora(ahora.hour, ahora.minute, ahora.second)   
    
  def hora_a_segundos (self) -> int:
    """ 
    PRE: 
      Hora.hora_a_segundos() -> int
    POST: 
      resultado: self en segundos
    """
    return self.hh*3600 + self.mm*60 + self.ss

  # @staticmethod  
  def segundos_a_hora (segs : int): 
    """ 
    PRE: 
      segundos_a_hora(int) -> Hora
    POST: 
      resultado: equivalente a segs segundos en Hora 
    """
    h = segs // 3600
    m = (segs % 3600) // 60
    s = (segs % 3600) % 60
    if h >= 24: h -= 24
    return Hora(h, m, s)

  def __sub__ (self, h): # -> Hora
    """ 
    PRE: 
      self >= h 
      Hora.resta(Hora) -> Hora
      Hora.__sub__(Hora) -> Hora
      Hora - Hora -> Hora
    POST: 
      resultado: self - h
    """
    segundos = self.hora_a_segundos() - h.hora_a_segundos()
    return Hora.segundos_a_hora(segundos)

  def __add__ (self, h): # -> Hora
    """ 
    PRE: 
      self >= h 
      Hora.suma(Hora) -> Hora
      Hora.__add__(Hora) -> Hora
      Hora - Hora -> Hora
    POST: 
      resultado: self + h
    """
    segundos = self.hora_a_segundos() + h.hora_a_segundos()
    return Hora.segundos_a_hora(segundos)

  def __eq__ (self, h) -> bool:
    """ 
    PRE: 
      Hora.es_igual(Hora) -> bool
      #Hora == Hora -> bool
    POST: 
      resultado: self es igual a h
    """
    return self.hh == h.hh and self.mm == h.mm and self.ss == h.ss
    
  def __lt__ (self, h) -> bool:
    """ 
    PRE: 
      Hora.es_menor(Hora) -> bool
      #Hora < Hora -> bool
    POST: 
      resultado: self es menor que h
    """
    return self.hh < h.hh or \
           (self.hh == h.hh and self.mm < h.mm) or \
           (self.hh == h.hh and self.mm == h.mm and self.ss < h.ss)


# Constructor:
h1 = Hora(0, 6, 7)
h2 = Hora(1, 6, 8) 
#h3 = Hora(1, 14, 0) 
#h4 = Hora(0, 0, 0) 

# Visualizadores:
#print("h1 =", h1)
#print("h2 =", h2)
#print("h3 =", h3)
#print("h4 =", h4)
#print("ahora = ", Hora.ahora())

# hora_a_segundos: 
#print("Hora(0, 0, 59).hora_a_segundos() =", Hora(0, 0, 59).hora_a_segundos())
#print("h1.hora_a_segundos() =", h1.hora_a_segundos())

# segundos_a_hora
#print("Hora.segundos_a_hora(3600) =", Hora.segundos_a_hora(3600))
#print("Hora.segundos_a_hora(24*60*60) =", Hora.segundos_a_hora(24*60*60))
#print("Hora.segundos_a_hora(24*60*60+1) =", Hora.segundos_a_hora(24*60*60+1))

# __add__  
#print("h1 + h2 =", h1.__add__(h2))
#print("h1 + h2 =", h1 + h2)  

# __sub__  
#print("h2 - h1 =", h2.__sub__(h1))
#print("h2 - h1 =", h2 - h1)  

# __eq__  
#print("h1 == h2 =", h1.__eq__(h2))
#print("h1 == h2 =", h1 == h2)  

# __lt__  
# print("h1 < h2 =", h1.__lt__(h2))
# print("h1 < h2 =", h1 < h2)  

