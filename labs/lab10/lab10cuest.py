class Automovil:
  """ 
    marca    : str
    capacidad : int   -- en litros, capacidad >= 0
    consumo   : float -- litros/100km, consumo >= 0
    deposito  : float -- gasolina en el deposito, en litros, 
                         deposito in {0..capacidad}
  """
  
  def __init__ (self, ma : str, ca : int, co : float):
    """ 
      Constructor de un Automovil: pone deposito a 0
    """
    self.ma = ma
    self.ca = ca
    self.co = co
    self.deposito = 0

  def __str__ (self) -> str:
    """ 
    POST: 
      resultado: Automovil como texto con formato:
                 <marca>, <capacidad> litros, <consumo> litros/100km
    """
    return f"{self.ma}: {self.ca} litros, {self.co} litros/100km"
    
  def distancia (self) -> float:
    """ 
    POST: resultado: distancia que puede alcanzar self con el depósito lleno
    """
    distancia = self.ca / self.co * 100
    return distancia

  def puede_llegar (self, d : float) -> bool:
    """ 
    POST: resultado: self puede alcanzar una distancia d con el depósito lleno
    """
    if self.distancia() >= d:
        return True
    else:
        return False
        
  def repostar (self, cantidad : float):
    """ 
    Carga el depósito con cantidad litros de gasolina
    """
    c = self.deposito + cantidad
    if c > self.ca:
        self.deposito = self.ca
    else:
        self.deposito = self.deposito + cantidad
    
    
  def __eq__ (self, a) -> bool:
    """ 
    PRE: 
      Automovil.es_igual(Automovil) -> bool
      #Automovil == Automovil -> bool
    POST: 
      resultado: self es igual a `a`: su marca, capacidad y consumo son iguales
    """
    if self.ma == a.ma and self.ca == a.ca and self.co == a.co:
        return True
    else:
        return False

a1 = Automovil('A', 30, 7)
a2 = Automovil('B', 40, 6)
a3 = Automovil('C', 35, 8)
auto1= Automovil('Ford', 40, 6)
auto2 = Automovil('Seat', 50, 5)

class Tiempo ():
  """
  Tiempo medido en minutos y segundos.
   
    mm : int -- minutos  -- mm >= 0
    ss : int -- segundos -- ss in {0..59}
  """
  
  def __init__ (self, mm : int, ss : int):
    """ 
    Constructor de Tiempo
    """
    self.mm=mm
    self.ss=ss
    
  def __str__ (self) -> str:
    """ 
    POST: resultado: Tiempo como texto con formato mm:ss     
    """
    return f"{self.mm:02d}:{self.ss:02d}"
    
  def tiempo_a_segundos (self) -> int:
    """ 
    POST: resultado: self en segundos
    """
    return self.mm*60 + self.ss

  # @staticmethod  
  def segundos_a_tiempo (segs : int): 
    """ 
    POST: resultado: equivalente a segs segundos en Tiempo
    """
    m = (segs//3600)*60
    s = (segs%3600)%60
    return Tiempo(m,s)
    
  def __sub__ (self, t):
    """ 
    PRE: 
      self >= t
    POST: 
      resultado: self - t
    """
    m = self.mm - t.mm
    s = self.ss - t.ss
    return Tiempo(m,s)
    
  def __add__ (self, t):
    """ 
    POST: 
      resultado: self + t
    """
    m = self.mm + t.mm
    s = self.ss + t.ss
    return Tiempo(m,s)
  def __eq__ (self, t) -> bool:
    """ 
    POST: 
      resultado: self es igual a t
    """
    return self.mm==t.mm and self.ss==t.mm
    
  def __lt__ (self, t) -> bool:
    """ 
    POST: 
      resultado: self es menor que t
    """
    return self.mm < t.mm or (self.mm == t.mm and self.ss < t.ss)
    
t1 = Tiempo(0, 6)
t2 = Tiempo(1, 6) 
t3 = Tiempo(1, 14) 
t4 = Tiempo(0, 0)

class Fraccion():
  """
  Una fracción num/den
    num : int -- numerador 
    den : int -- denominador  -- den > 0
  """
  def __init__ (self, num : int=0, den : int=1):
    """
    PRE: den > 0
    
    Constructor de una Fraccion
    """
    self.num = num
    self.den = den
    
  def __str__ (self) -> str:
    """ 
    POST: 
      resultado: Hora como texto      
    """
    return str(self.num) + "/" + str(self.den) 
    
  def __add__ (self, f): 
    """ 
    PRE: f : Fraccion
    POST: resultado: self + f
    """
    nuevo_num = self.num * f.den + f.num * self.den
    nuevo_den=self.den * f.den
    return Fraccion(nuevo_num,nuevo_den)
    
  def sim (self): 
    """ 
    POST: resultado: self simplificada
    """
    divisor_comun = self.mcd(self.num,self.den)
    
  def mcd (a : int, b : int) -> int:
    """ 
    PRE: a >= 1, b >= 1
    POST: resultado: MCD de a y b
    POST: resultado: x in {1..min(a, b)}. (a%x=0 and b%x=0)
    """
    encontrado = False
    i = min(a, b)
    while i >=1 and not encontrado:
      if a%i==0 and b%i==0: 
        encontrado = True
      else:
        i -= 1
    return i

def suma_serie (n : int) -> Fraccion:
  """ 
  PRE: n >= 1
  POST: resultado: 1 + 1/2 + 1/3 +...+ 1/n
        La fracción resultado se da simplificada
  EJEMPLO:      
    suma_serie(3) --> Fraccion(11, 6)
  """
  a = Fraccion (1,1)
  for i in range (2,n+1):
    a += Fraccion (1,i)
  return a