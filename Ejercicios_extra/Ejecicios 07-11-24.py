def existe(l:list, n:int) -> bool:
    a = False
    i = 0
    while i <= len(l)-1 and not a:
        if l[i]== n:
            a=True    
        else:
            i+=1
    return a

def posicion (l:list, n:int) -> int:
    existe = False
    i=0
    while i <= len(l)-1 and not existe:
        if l[i] == n:
            existe = True
        else:
            i+=1
    return i
            


def todos (l:list, n:list) -> bool:
    todos=True
    i=0
    while i <= len(l)-1 and todos:
        if not(l[i] == n):
            todos = False
        else:
            i+=1
    return todos
    
def frecuencia (n:int, l:list) -> int:
    """
    POST: resultado: el numero de veces que aparece "n" en "lista"
  """
    cont=0
    for e in l:
        if e == n: cont+=1
    return cont
    
#Funcion hay_repetidos, recibe una lista de enteros, 
#y determina si existe al menos un numero que aparezzca repetido en la lista.

def hay_repetidos(l:list) -> bool:
    i=0
    a = False
    while i<=len(l)-1 and not a:
        if frecuencia(l[i], l) > 1:
            a = True
        else:
            i+=1
    return a
            