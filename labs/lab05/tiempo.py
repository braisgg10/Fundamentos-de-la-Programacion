""" 
clase Tiempo para lab05
No es necesario que los estudiantes lean, editen o comprendan este programa.
"""

class Tiempo (object):
  """
  Las instancias representan un Tiempo con una resolución de minutos.
  
  Atributos:
    horas [int no negativo]: número de horas
    minutos [int en el rango 0..59]: número de minutos
  """

  ## ESTUDIANTES: no os preocupéis por la sintaxis de esta definición de método.
  ## Sólo se necesita saber que una llamada de la forma Tiempo(x,y)
  ## establecerá el nuevo Tiempo con x horas e y minutos.
  
  def __init__(self, h : int, m : int):
    """
    Crea un objeto Tiempo con h horas y m minutos
    PRE: h >= 0, m in 0..59
    """
    self.horas = h
    self.minutos = m