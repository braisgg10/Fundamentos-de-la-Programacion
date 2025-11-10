# Fecha.py

""" 
  Contiene una clase Fecha 
"""

from datetime import datetime

class Fecha ():
  """
  Fecha: medida del tiempo en días, meses y años, asumiendo que hay 12 meses y 
         un mes tiene dias_mes(mes, año) días
      
    d : int -- día -- d in {1..dias_mes(m, a)} 
    m : int -- mes -- m in {1..12}
    a : int -- año 
  """
  
  def __init__ (self, d : int, m : int, a : int):
    """ 
    PRE: 
      Fecha(int, int, int) -> Fecha
      
    Constructor de una Fecha
    """
    self.d = d;
    self.m = m;
    self.a = a;
    
  def __str__ (self) -> str:
    """ 
    PRE: 
      str() -> str
    POST: 
      resultado: Fecha como texto      
    """
    return f"{self.d:02d}/{self.m:02d}/{self.a:02d}"
    
  # @staticmethod  
  def hoy (): 
    """ 
    PRE: 
      hoy () -> Fecha
    POST: 
      resultado: la Fecha de hoy
    """
    hoy = datetime.now()
    return Fecha(hoy.day, hoy.month, hoy.year)   
    
  def es_bisiesto (a : int) -> bool: 
    """ 
    POST: resultado: POST: "año es bisiesto"
    POST: resultado: año es un multiplo de 4 que no es el año 0 de un siglo o 
                     es un multiplo de 400 
    """
    if a%4==0 and a%100!=0 or a%400==0:
        return True
    else:
        return False
        
  def dias_febrero (a : int) -> int:
    """ 
    POST: resultado: POST: "año es bisiesto"
    POST: resultado: el número de días que tiene el mes de Febrero de a
    """
    if a == True:
        return 29
    else:
        return 28
        
  def dias_mes (m : int, a : int) -> int:
    """ 
    PRE: m in {1..12}
    POST: 
      resultado: el número de días del mes m (para este año a en el caso 
                 de Febrero)
    POST:
       resultado: m in {4, 6, 9, 11} --> 30
                  m in {1, 3, 5, 7, 8, 10, 12} --> 31
                  m = 2 --> dias_febrero(a)
    """
    if m in [4,6,9,11]:
        return 30
    elif m in [1,3,5,7,8,10,12]:
        return 31
    elif m==2:
        return Fecha.dias_febrero(a)
    
  def siguiente (self):
    """ 
    PRE: 
      Fecha.siguiente() -> Fecha
    POST: 
      resultado: Fecha siguiente a self 
    """
    if self.d < Fecha.dias_mes(self.m, self.a):
      return Fecha(self.d + 1, self.m, self.a)
    elif self.d == Fecha.dias_mes(self.m, self.a) and self.m < 12:
      return Fecha(1, self.m + 1, self.a)
    else:
      return Fecha(1, 1, self.a + 1)
   
  def __eq__ (self, f) -> bool:
    """ 
    PRE: 
      Fecha.es_igual(Fecha) -> bool
      #Fecha == Fecha -> bool
    POST: 
      resultado: self es igual a f
    """
    return self.d==f.d and self.m==f.m and self.a==f.a
  def __lt__ (self, f) -> bool:
    """ 
    PRE: 
      Fecha.es_menor(Fecha) -> bool
      #Fecha < Fecha -> bool
    POST: 
      resultado: self es menor que f
    """
    if self.a==f.a:
        if self.m==f.m:
            return self.d<f.d
        else:
            return self.m<f.m
    else:
        return self.a<f.a
    
# Constructor:
f1 = Fecha(30, 6, 2008) 
f2 = Fecha(1, 1, 2000) 

# Visualizadores:
print("f1 =", f1)
print("f2 =", f2)
print("hoy = ", Fecha.hoy())

# siguiente
print("f1.siguiente() =", f1.siguiente())

# __eq__  
print("f1 == f2 =", f1.__eq__(f2))
print("f1 == f2 =", f1 == f2)  

# __lt__  
print("f1 < f2 =", f1.__lt__(f2))
print("f1 < f2 =", f1 < f2)  
