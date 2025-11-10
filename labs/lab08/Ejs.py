def borrado_una (lista:list, a:str) -> list:
    """
    EJEMPLOS:
        (["una", "dos", "una", "dos"], "una") -> ["dos", "dos"]
        (["dos, "tres", "cuatro], "una") -> ["dos, "tres", "cuatro]
        ([], "una") -> []
   """
    res = []
    for i in lista:
        if i != a:
            res += [i]
    return res
    
#PARA BORRAR ELEMENTOS DE UNA LISTA
#    1) lista.remove(i)
#    2) del lista[i]

def borrado_varias(lista: list, a_borrar:list) -> list:
    """
    Recibe dos listas, la de entrada y la q contiene los elementos a borrar
   """
    res=[]                                  #res = lista
    for i in lista:                         #for e in a_borrar:
        if i not in a_borrar:               #   res=borrado_una(res, e)
            res += [i]                      #return res
    return res


def frecuencia (n:int, l:list) -> int:
    """
    POST: resultado: el numero de veces que aparece "n" en "lista"
   """ 
    cont=0
    for e in l:
        if e == n: cont+=1
    return cont

def hay_repetidos (lista:list) -> bool:
    existe = False
    i = 0
    while i < len(lista) and not existe:
        if frecuencia(lista[i], lista) >= 2:
            existe = True
        else: i += 1
    return existe

#una funcion que me dice si una lista de numeros está ordenada
def esta_ordenada (lista:list) -> bool:
    ordenada= True
    i=0
    while i <= len(lista)-2 and ordenada:
        if lista[i] > lista[i+1]:
            ordenada=False
        else:
            i+=1
    return ordenada
    
def es_primo(a:str) -> bool:
    primo= True
    i=2
    while i < a and primo:
            if a%i==0:
                primo = False
            else:
                i+=1
    return primo
    
#una funcion que me devuelve una lista entre dos y n
def primos (a:str) -> list:
    res=[]
    for i in range (2,a+1):
        if es_primo(i)==True:
            res+=[i]
    return res

def suma_intervalo(a:int, b:int) -> int:
    suma = 0
    for i in range (a,b+1):
        suma+= i
    return suma

def es_triangular (n:int) -> bool:
    existe=False
    k=0
    while k <= n and not existe:
        if suma_intervalo(1,k) == n:
            existe = True
        else:
            k+=1
    return existe

def cuantos_triangulares(n:int) -> int:
    ct=0
    for i in range(1,n+1):
        if es_triangular(i) == True:
            ct+=1
        else:
            ct=ct
    return ct
def triangulares(n:int) -> list:
    res = []
    ct = 0
    i = 1
    while ct < n:
        if es_triangular(i) == True:
            res += [i]
            ct += 1
            i += 1
        else:
            i+=1
    return res