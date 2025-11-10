def distancia_media (lp:list, p: Punto) -> float:
    suma = 0
    for pun in lp:
        suma += p.distancia(pum)
    if len(lp) == 0:
        return 0
    else:
        return suma/len(lp)
def nube (n:int) -> list:
    """
    PRE: (int) -> list[Punto]
    POST: resultado: una lista con una nube de n puntos aleatorios
    """
    res = []
    for i in range (1,n+1):
        res+= [punto_alea()]
    return res