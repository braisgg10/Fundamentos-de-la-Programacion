# poblacion.py
  
""" 
  Contiene una clase Localidad y operaciones de manejo
"""

class Localidad:
  """
    nombre : str    -- nombre de la Localidad
    poblacion : int -- número de habitantes, poblacion >= 0
  """
  
  def __init__ (self, nombre : str, poblacion : int):
    """     
    PRE: (str, int) -> Localidad
    
    Constructor de una Localidad
    """
    self.nombre = nombre
    self.poblacion = poblacion

  def __str__ (self) -> str:
    """ 
    POST: resultado: Localidad como texto      
    """
    return f"La localidad {self.nombre} tiene {self.poblacion} habitantes"
    
  def str_a_localidad (linea : str):
    """ 
    PRE: linea es un str con el formato:
         Sexo;Provincia;Municipio;Fecha;Total
    DONDE:
      - Municipio: nombre del municipio
      - Total: población total del municipio
  
    POST: (str) -> Localidad
          resultado: Localidad(Municipio, Total)
    """
    elementos = linea.split(";")
    return Localidad(elementos[2], int(elementos[4]))
    
  def __lt__ (self,otra) -> bool:
    """
    POST: resultado: self < otra
    """
    return self.poblacion < otra.poblacion
        
def to_string (lista : list) -> str:
  """ 
  PRE: (list[Localidad]) -> str

  POST: resultado: lista como un texto con el formato:
                   [loc_1,
                    loc_2, 
                    ...]
  """
  return "[\n" + "\n".join(str(loc) for loc in lista) + "\n]"
  
def carga (nombre_fichero : str) -> list:
  """ 
  POST: (str) -> list[Localidad]
        resultado = lista de Localidad(es) que aparecen en el fichero
                    de nombre nombre_fichero
  """
  fichero = open(nombre_fichero)
  lista = fichero.readlines()
  lista = lista[2:] #Saltar las dos primeras líneas
  locs = []
  for linea in lista:
    locs += [Localidad.str_a_localidad(linea)]
  fichero.close()
  return locs


def posicion (nom : str, locs : list) -> int:
  """ 
  PRE: (str, list[Localidad]) -> int

  POST: resultado: la posición que ocupa en locs la Localidad cuyo nombre es 
                   nom, y si no se encuentra, devuelve -1 
  """
  for i in range (len(locs)):
    if locs[i].nombre == nom:
      return i
  return -1
    
def poblacion (loc: Localidad) -> int:
    return loc.poblacion
    

def poblacion_conjunta (locs : list, 
                        comunidad : list) -> int:
  """ 
  PRE: locs : list[str], comunidad : list[Localidad]

  POST: resultado: la población total del grupo de localidades de comunidad 
                   cuyos nombres vienen en locs
  """
  total = 0
  for i in locs:
      pos = posicion(i, comunidad)
      if pos != -1:
          total += comunidad[pos].poblacion
  return total

def carga_test ():
  locs = carga("cam_municipios_poblacion_2022.csv")
  print(to_string(locs))
  locs.sort(key=poblacion)
  print(to_string(locs))

def poblacion_conjunta_test ():
  comunidad = carga("cam_municipios_poblacion_2022.csv")
  locs = ["Alcorcón", "Móstoles", "Leganés", "Fuenlabrada"]
  print("locs =", locs)
  print("poblacion_conjunta =", poblacion_conjunta(locs, comunidad))

def main ():
  carga_test()
  # poblacion_conjunta_test()
  
if __name__ == '__main__': 
  main()
  
 