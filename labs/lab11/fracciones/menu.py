# menu.py

class Menu:
  """
    Menu con lista de opciones:
      opciones : list[str] -- Lista de opciones
  """ 
  def __init__ (self, ops : list):
    """
    PRE: (list[str]) -> Menu
    
    POST: resultado: el Menu creado con las opciones ops
    """
    self.opciones = ops
  
  def es_opcion_valida (self, opcion : str) -> bool:
    """
    POST: resultado: la opcion está en el rango de opciones
    """
    return 1 <= int(opcion) <= len(self.opciones)
    
  def leer_opcion (self) -> str:
    """
    POST: resultado: la opcion leída del usuario,
          es_opcion_valida(resultado)
    """
    opcion = input("\n" + "Seleccione una de las opciones para continuar: ")
    while not self.es_opcion_valida(opcion):
      opcion = input("\n" + "Seleccione una de las opciones para continuar: ")
    return opcion
  
  def mostrar_opciones (self):
    """
    Muestra las opciones del menú con el formato:
    
      <i>. <opcion>, i in {1..len(opciones)}, opcion = opciones[i]
    """
    print()
    for i in range(len(self.opciones)):
      print(f"{i+1:d}. {self.opciones[i]:s} ")
  

