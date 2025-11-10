def es_bisiesto(a: int) -> bool:
    """
    PRE: a>=0
    POST: "el año a es bisiesto"
    """
    return a%4==0 and a%100!=0 or a%400==0
    
    
def dias_febrero (a: int) -> int:
    if es_bisiesto(a) == True:
        return 29
    else:
        return 28
        
def coste_lapiz (lapices: int) -> float:
    """
    PRE: lapices >= 0
    POST: resultado: coste de un lápiz en céntimos de euro según la
          cantidad de lapices pedida
    """
    if lapices >= 1000:
        return 0.85
    else:
        return 0.90
        
def coste_total (lapices:int) -> float:
    """
    PRE: lapices >= 0
    POST: resultado: coste de un pedido de una cantidad de lapices en euros
    """
    if lapices >= 1000:
        return lapices*0.85
    else:
        return lapices*0.9

def calculo (op1 : int, oper : str, op2 : int) -> int:
    """
    PRE: oper in {'+', '-', '*', '/'}
    POST:
    resultado:
    oper = '+' --> op1 + op2
    oper = '-' --> op1 - op2
    oper = '*' --> op1 * op2
    oper = '/' --> op1 // op2
    """
    if oper == "+":
        return op1+op2
    if oper == "-":
        return op1-op2
    if oper == "*":
        return op1*op2
    if oper == "/":
        return op1//op2



PRECIO_NORMAL = 30
PRECIO_REDUCIDO = 25
PRECIO_MUY_REDUCIDO = 20
def precio_menu (asistentes : int) -> float:
    
    """
    PRE: asistentes >= 0
    POST: resultado: el precio de un menú en euros según el número de asistentes
    al evento
    """
    if asistentes < 200:
      return PRECIO_NORMAL
    if asistentes >= 200 and asistentes <= 300:
      return PRECIO_REDUCIDO
    if asistentes > 300:
        return PRECIO_MUY_REDUCIDO

def coste_totalm (asistentes : int) -> float:
    """
    PRE: asistentes >= 0
    POST: resultado: el coste total en euros de todos los menús de un evento
    según el número de asistentes
    """
    if asistentes < 200:
      return PRECIO_NORMAL*asistentes
    if asistentes >= 200 and asistentes <= 300:
      return PRECIO_REDUCIDO*asistentes
    if asistentes > 300:
        return PRECIO_MUY_REDUCIDO*asistentes

    
