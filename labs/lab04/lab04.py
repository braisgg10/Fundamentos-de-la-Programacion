""" 
  Contiene una funcion util para strings 
"""
 
def cambia_primero (palabra : str, objetivo : str, nuevo : str) -> str: 
  """
  PRE: objetivo tiene una longitud ≥ 1 y aparece al menos una vez en palabra
  POST:
     resultado: una copia del string palabra con la primera aparición del 
                string objetivo en palabra reemplazada por el string nuevo. 
  EJEMPLOS: 
    cambia_primero('GraciaS', 'S', 's') --> 'Gracias'
  """
  pos = palabra.index(objetivo)  # donde empieza el primer objetivo 
  #print ("DEPURACIÓN: pos= " + str(pos))
  antes = palabra[:pos]  # parte de palabra hasta objetivo, sin incluirlo
  #print ("DEPURACIÓN: antes= " + str(antes))
  despues = palabra[pos+ len(objetivo):]  # parte de palabra despues de objetivo
  #print ("DEPURACIÓN: despues= " + str(despues))
  result = antes + nuevo + despues  # salida deseada
  #print ("DEPURACIÓN: result= " + str(result))
  return result
  
def primera_mitad(palabra: str) -> str:
    return palabra[:int(len(palabra))//2]

def sin_inicio_fin(palabra: str) -> str:
    return palabra [1:int(len(palabra)-1)]
    
def sin_inicio(p1: str, p2: str) -> str:
    return (p1[1:len(p1)]) + (p2[1:len(p2)])

def filtro (palabra: str) -> str:
    p1= palabra.strip()
    p2= p1.strip(",.:;")
    return p2.lower()

def cuadro (car:str, n:int) -> str:
    return car*n
    
def linea (uno:str, otro:str, m: int, n:int) -> str:
    return (uno*m +otro*m) *n
   
def tablero (uno:str, otro:str, m:int, n:int) -> str:
    línea1 = str((uno*m + otro*m)*(n//2) + "\n" + (otro*m + uno*m)*(n//2) + "\n")
    return (línea1*(n//2))
    
    #return ((uno*m + otro*m)*int(n/2) \n ((otro*m+uno*m)*int(n/2) \n)) *int(n/2)