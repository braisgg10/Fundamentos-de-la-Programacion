# figuras.py
""" 
  Figuras del juego rompemuros
"""

from pygame import Color

class Rectangulo ():
  """
  Un rectángulo en el espacio 2D 
    x     : float -- coord x del vértice inferior izquierdo 
    y     : float -- coord y del vértice inferior izquierdo 
    ancho : float -- anchura del rectangulo
    alto  : float -- altura del rectangulo
  """
  
  def __init__(self, x : float, y : float, ancho : float, alto : float):
    """   
    resultado: un Rectangulo creado
    """
    self.x = x
    self.y = y
    self.ancho=ancho
    self.alto=alto
 
  def __str__ (self):
    """
    resultado: este Rectangulo convertido en texto 
    """
    return f"Tu rectángulo está en centrado ({self.x},{self.y}) \
    y tiene {self.ancho} de ancho y {self.alto} de alto."
    
  def mover (self, dx : float, dy : float):
    """ 
    mueve este Rectangulo según (dx, dy)
    """
    self.x += dx
    self.y += dy
    
  def ancho (self) -> float:
    """
    resultado: el ancho de este Rectangulo 
    """
    return self.ancho
    
class Ladrillo (Rectangulo):
  """
  Un ladrillo es un rectángulo con Color
    color : Color -- color del ladrillo
  """
  
  def __init__(self, x : float, y : float, \
               ancho : float, alto : float, color : Color):
    """   
    resultado: un Ladrillo creado
    """
    super().__init__(x, y, ancho, alto)
    self.color = color
      
  def __eq__ (self, otro) -> bool:
    """ 
    PRE: otro : Ladrillo
    
    POST: resultado: self es igual (por contenido) a otro 
    """
    return super().__eq__(otro) and self.color == otro.color

    
class Paleta (Rectangulo):
  """
  Una Paleta es un Rectangulo con Color
    color : Color -- color de la Paleta
  """
  
  def __init__(self, x : float, y : float, \
               ancho : float, alto : float, color : Color):
    """   
    resultado: una Paleta creada
    """
    super().__init__(x, y, ancho, alto)
    self.color = color
    
  def __eq__ (self, otro) -> bool:
    """ 
    PRE: otro : Paleta
    
    POST: resultado: self es igual (por contenido) a otro 
    """
    return super().__eq__(otro) and self.color == otro.color
    
  def mover (self, dx : float, n : int):
    """
    mueve esta Paleta según dx en el rango -n..n
    """
    super().mover(dx, 0)
    if not self.esta_dentro_der(dx, n):
      self.x = n - super().ancho()
    if not self.esta_dentro_izq(dx, n):
      self.x = 0
    
  def esta_dentro_der (self, dx : float, n : int) -> bool:
    return self.x + dx + super().ancho() <= n 
    
  def esta_dentro_izq (self, dx : float, n : int) -> bool:
    return self.x + dx >= 0   
    

class Circulo ():
  """
  Un Circulo en el espacio 2D 
    x     : float -- coord x del centro
    y     : float -- coord y del centro
    radio : float -- radio del Circulo, radio >= 0
  """
  
  def __init__(self, x : float, y : float, radio : float):
    """   
    resultado: un Circulo creado
    """
    self.x = x
    self.y = y
    self.radio = radio
    
  def __str__ (self):
    """
    resultado: este Circulo convertido en texto 
    """
    return "(" + str(self.x) + ", " + str(self.y) + ", " +\
                 str(self.radio) + ")"

  def mover (self, dx : float, dy : float):
    """ 
    mueve este Circulo según (dx, dy)
    """
    self.x += dx
    self.y += dy
    
  def radio (self) -> float:
    return self.radio

class Bola (Circulo):
  """
  Una Bola es un Circulo con velocidad (vx, vy) y Color
    vx : float -- velocidad en x 
    vy : float -- velocidad en y
    color : Color -- color de la Bola
  """
  
  def __init__(self, x : float, y : float, \
               radio : float, vx : float, vy : float, color : Color):
    """   
    resultado: una Bola creada
    """
    super().__init__(x, y, radio)
    self.vx = vx
    self.vy = vy
    self.color = color
      
  def mover (self, nx : int, ny : int):
    """
    mueve esta Bola según vx y vy en el rango 0..n
    """
    super().mover(self.vx, self.vy)
    self.rebotar_pared(nx, ny)
    
  def esta_dentro_x (self, n : int) -> bool:
    return self.x + self.vx >= 0 and self.x + self.vx  <= n 

  def esta_dentro_y (self, n : int) -> bool:
    return self.y + self.vy >= 0 and self.y + self.vy  <= n 
    
  def rebotar_pared (self, nx : int, ny : int):
    if not self.esta_dentro_x(nx): self.vx = -self.vx
    if not self.esta_dentro_y(ny): self.vy = -self.vy

  def cambiar_dir (self): 
    self.vx = -self.vx
    self.vy = -self.vy
    
  def choca (self, r) -> bool:
    """
    PRE: r : Rectangulo
    POST: resultado: esta Bola choca con r
    """
    eje_x = max (r.x, min(self.x, r.x + r.ancho))
    eje_y = max (r.y, min(self.y, r.y + r.alto))
    distancia = ((self.x - eje_x)**2 + (self.y - eje_y) ** 2) ** 0.5
    return distancia <= self.radio
    
  def rebotar (self, r):
    """
    PRE: r : Rectangulo
    """
    if self.choca(r):
      self.vy = -self.vy  
      
  def toca_suelo (self, n : int) -> bool:
    return self.y + self.radio >= n
    