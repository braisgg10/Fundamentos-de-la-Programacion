def calificacion (a:float) -> str:
    """
    PRE: a tiene que ser <= que 0 y >= que 10.
    POST: devuelve "B", "N", "A" o "S" en función de tu calificación.
    """
    if a >= 9 and a <= 10:
        return "B"
    if a < 9 and a >= 7:
        return "N"
    if a < 7 and a >= 5:
        return "A"
    if a < 5 and a >= 0:
        return "S"
        
        
def nota_fp (labs : float, parcial : float, examen : float) -> float:
    """
  PRE: labs>=0, parcial>=0, examen>=0
  POST: resultado:
  examen < 4 --> examen
  examen >= 4 --> max(examen, 0.3*labs + 0.1*parcial + 0.6*examen)
  EJEMPLOS:
  nota_fp(6, 7, 3.5) --> 3.5
  nota_fp(7, 7, 4) --> 5.2
  nota_fp(0, 4, 7) --> 7
    """
    if examen < 4:
        return examen
    if examen >= 4:
        return max(examen, 0.3*labs + 0.1*parcial + 0.6*examen)


def calificacion_fp (labs : float, parcial : float, examen : float) -> str:
    if nota_fp(labs, parcial, examen) >= 9 and nota_fp(labs, parcial, examen) <= 10:
        return "B"
    elif nota_fp(labs, parcial, examen) < 9 and nota_fp(labs, parcial, examen) >= 7:
        return "N"
    elif nota_fp(labs, parcial, examen) < 7 and nota_fp(labs, parcial, examen) >= 5:
        return "A"
    elif nota_fp(labs, parcial, examen) < 5 and nota_fp(labs, parcial, examen) >= 0:
        return "S"
        
        
def en_rango (n: int) -> bool:
    return 10<= n <= 20
    


def max_10_20 (a: int, b: int) -> int:
    if en_rango(a)==True and en_rango(b)==True:
        return max(a,b)
    if en_rango(a)==True and en_rango(b)==False:
        return a
    if en_rango(a)==False and en_rango(b)==True:
        return b
    if en_rango(a)==False and en_rango(b)==False:
        return 0



def que_posicion (x: int, y: int) -> str:
    if x == 0 and y == 0:
        return "ORIGEN"
    elif x==0 or y==0:
        return "EJES"
    elif x>0 and y>0:
        return "PRIMERO"
    elif x<0 and y>0:
        return "SEGUNDO"
    elif x<0 and y<0:
        return "TERCERO"
    elif x>0 and y<0:
        return "CUARTO"


def es_bisiesto(a: int) -> bool:
    """
    PRE: a>=0
    POST: "el año a es bisiesto"
    """
    return a%4==0 and a%100!=0 or a%400==0


def dias_mes (a:int, b:int) -> int:
    if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
        return 31
    elif a == 4 or a == 6 or a == 9 or a == 11:
        return 30
    elif a==2:
        if es_bisiesto (b) == True:
            return 29
        else:
            return 28
    else:
        return False

def es_fecha_correcta(a: int, b: int, c: int) -> bool:
    if a > 0 and a <= 31 and b > 0 and b <= 12 and c >= 0:
        if b==2:
            if es_bisiesto(c) == True and a <= 29:
                return True
            elif es_bisiesto(c) == True and a > 29:
                return False
        elif dias_mes (b,c) == 31 and a <= 31:
            return True
        elif dias_mes (b,c) == 30 and a <= 30:
            return True
        else:
            return False
    else:
        return False


def es_menor_o_igual (d1 : int, m1 : int, a1 : int, d2 : int, m2 : int, a2 : int) -> bool:
    if d1==d2 and m1 == m2 and a1 == a2:
        return True
    elif a1 < a2:
        return True
    elif a1 == a2 and m1 < m2:
        return True
    elif a1 == a2 and m1 == m2 and d1 < d2:
        return True
    else:
        return False

        



def descuento(precio: float) -> float:
    if precio > 500:
        return precio*0.85
    else:
        return precio
        
        
def inverso (s: str) -> str:
    t= ""
    for c in s:
        t= c+t
    return t


def factorial (a: int) -> int:
    f = 1
    for i in range (1, a+1):
        f *= i #f = f * i  
    return f
