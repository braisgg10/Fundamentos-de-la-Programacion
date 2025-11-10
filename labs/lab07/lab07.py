def desplaz (s : str) -> str:
    p = ""
    for i in range(len(s)):
        p += s[i:] + s[:i] + "\n"
    return p.strip()
    
    
    
def es_bisiesto(a: int) -> bool:
    """
    PRE: a>=0
    POST: "el año a es bisiesto"
    """
    return a%4==0 and a%100!=0 or a%400==0

def cuantos_bisiestos(inicio: int, fin: int) -> int:
    t=0
    for i in range (inicio, fin+1):
        if es_bisiesto(i) == True:
            t+=1 #t= t+1
        else:
            t+=0
    return t
    
def dias_en_media(inicio: int, fin:int) -> float:
    m=0
    if inicio > fin:
        return 0
    else:
        for i in range (inicio, fin+1):
            if es_bisiesto(i) == True:
                m+=366
            else:
                m+=365
        return m / ((fin-inicio)+1)
        

from random import randint
from random import uniform
def estimacion_pi (n:int) -> float:
    """
    PRE: n >= 0
    POST: resultado: una estimación del número Pi generando números aleatorios dentro de un cuadrado de dimensiones 2x2
    """
    ct=0
    for i in range(n):
        x = uniform (-1,1)
        y = uniform (-1,1)
        if x**2 + y**2 <= 1:
            ct=ct+1
        else:
            ct=ct
        pi=4*(ct/n)
    print(ct)
    return pi
    
    
    
