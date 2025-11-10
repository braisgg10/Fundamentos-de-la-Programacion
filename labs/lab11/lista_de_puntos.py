from math import sqrt

#([(-1,1),(1,1),(1,-1),(-1,-1),(-1,1)])
def es_poligono(ldp: list) -> bool:
    if len(ldp)<3:
        return False
    return ldp[0] == ldp [-1]

def perimetro_poligono (ldp:list) -> float:
    p = 0
    for i in range (len(ldp) -1):
        p += sqrt((ldp[i+1][0] - ldp[i][0])**2 + (ldp[i+1][1] - ldp[i][1])**2)
    return p
    
def movimiento (ldp:list, dx: float, dy:float) -> list:
    a = []
    for i in range (len(ldp)):
        b = ldp[i][0] + dx
        c = ldp[i][1] + dy
        a.append((b,c))
    return a

def mover (ldp:list, dx: float, dy:float):
    a = []
    for i in range (len(ldp)):
        b = ldp[i][0] + dx
        c = ldp[i][1] + dy
        a.append((b,c))
    ldp = a

def filtro_origen (ldp:list) -> list:
    # a=[]
    # for i in range (len(ldp)):
        # if ldp[i] != (0,0):
            # a.append (ldp[i])
    # return a
    a = []
    for i in ldp:
        if i != (0,0):
            a.append(i)
    return a

def max_suma (ldp:list) -> list:
    max_punto=ldp[0]
    max_suma_coord = max_punto[0] + max_punto[1]
    for i in ldp:
        suma = i[0] + i[1]
        if suma > max_suma_coord:
            max_suma_coord = suma
            max_punto = i
    return max_punto

def existe_origen (ldp:list) -> bool:
    for i in ldp:
        if i == (0,0):
            return True
    return False

def posicion_punto (ldp:list, a:tuple) -> int:
    for i in range (len(ldp)):
        if ldp[i] == a:
            return i
    return -1
def todos_origen (ldp:list) -> bool:
    es=True
    i = 0
    while i < len(ldp) and es:
        if ldp[i] == (0,0):
            i+=1
        else:
            es = False
    return es
        