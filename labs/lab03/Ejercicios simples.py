def es_bisiesto(a: int) -> bool:
    """
    PRE: a>=0
    POST: "el año a es bisiesto"
    """
    return a%4==0 and a%100!=0 or a%400==0
    
def es_par (a: int) -> bool:
     return a%2==0

def último_dígito (a: int) -> int:
    return a%10

def es_letra (x: str) -> bool:
    """
    PRE: elargumento, x,  tiene que estar entre comillas, es decir "x".
    """
    return "a" <= x and x <= "z"

def hora (a: int) -> bool:
    """
    Pre: Introduce 6 dígitos (hhmmss)
    """
    return (0 <= a//10000 <= 23) and (0 <= ((a%10000)-(a%100))//100 <= 59) and (0 <= a%100 <= 59)

def coste(precio: float, porcentaje: float) -> float:
    return (precio + precio*(porcentaje/100))

