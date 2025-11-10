import math

def es_multiplo (a : int, b: int) -> bool:
    return a%b==0
    
def distancia (x1, y1, x2, y2 : float) -> float:
    return math.sqrt(((x2-x1)**2)+((y2-y1)**2))    

 
def pulgadas_a_cm (d : float) -> float:
    return d*2.54
    
def pies_a_cm (d : float) -> float:
    return d*12*2.54
        
def centimetros (d_pies : float, d_pulgadas : float) -> float:
    return d_pies*12*2.54+d_pulgadas*2.54

def dif_total (entrada : int, salida : int) -> int:
    return (salida//100 * 60 + salida%100) - (entrada//100*60 + entrada%100)
    
def dif_horas (entrada: int, salida: int) -> int:
    return ((salida//100 * 60 + salida%100) - (entrada//100*60 + entrada%100))//60
    
def dif_minutos (entrada : int, salida : int) -> int:
    return ((salida//100 * 60 + salida%100) - (entrada//100*60 + entrada%100))%60   
    
def horas (n : int) -> int:
    return n//3600

def minutos (n : int) -> int:
    return (n-(n//3600)*3600)//60

def segundos (n : int) -> int:
    return (n-(n//3600)*3600)%60

def horas_minutos_segundos (n : int) -> str:
    return str(n//3600) + "h " + str((n-(n//3600)*3600)//60) + "m " + str((n-(n//3600)*3600)%60) + "s"
 
    
