def acertar():
    frase_original_texto= "ser o no ser"
    frase_original= frase_original_texto.split()
    lista_cambios= [0,3,7]
    frase_a_rellenar=frase_huecos(frase_original, lista_cambios)
    frase_rellena= frase_usuario(frase_a_rellenar)
    aciertos=aciertos(frase_original, frase_rellena, lista_cambios)
    
from stddraw import *
from color import Color

def dibujar_baldosa(x0:float, y0:float, lado:float):
    """
    PRE: lado >= 0
    Dibuja una baldosa diseñada de lado x lado con su centro en (x0, y0).
  """
    setXscale(x0-lado/2,x0+lado/2)
    setYscale(y0-lado/2,y0+lado/2)
    
    setPenColor(CYAN)
    filledSquare(x0-lado*3/8, y0+lado*3/8, lado/8)
    filledSquare(x0+lado*3/8, y0+lado*3/8, lado/8)
    filledSquare(x0+lado*3/8, y0-lado*3/8, lado/8)
    filledSquare(x0-lado*3/8, y0-lado*3/8, lado/8)
    
    setPenColor(RED)
    filledSquare(x0-lado/8, y0+lado*3/8, lado/8)
    filledSquare(x0+lado/8, y0+lado*3/8, lado/8)
    filledSquare(x0-lado/8, y0-lado*3/8, lado/8)
    filledSquare(x0+lado/8, y0-lado*3/8, lado/8)
    filledSquare(x0-lado*3/8, y0+lado/8, lado/8)
    filledSquare(x0-lado*3/8, y0-lado/8, lado/8)
    filledSquare(x0+lado*3/8, y0+lado/8, lado/8)
    filledSquare(x0+lado*3/8, y0-lado/8, lado/8)
    
    setPenColor(YELLOW)
    filledPolygon([x0-lado/2, x0-lado/4, x0-lado*3/8], [y0+lado/4, y0+lado/4, y0+lado/8])
    filledPolygon([x0-lado/2, x0-lado/4, x0-lado*3/8], [y0-lado/4, y0-lado/4, y0-lado/8])
    filledPolygon([x0-lado/4, x0-lado/4, x0-lado/8], [y0-lado/4, y0-lado/2, y0-lado*3/8])
    filledPolygon([x0+lado/4, x0+lado/4, x0+lado/8], [y0-lado/4, y0-lado/2, y0-lado*3/8])
    filledPolygon([x0+lado/4, x0+lado/2, x0+lado*3/8], [y0-lado/4, y0-lado/4, y0-lado/8])
    filledPolygon([x0+lado/4, x0+lado/2, x0+lado*3/8], [y0+lado/4, y0+lado/4, y0+lado/8])
    filledPolygon([x0+lado/4, x0+lado/4, x0+lado/8], [y0+lado/4, y0+lado/2, y0+lado*3/8])
    filledPolygon([x0-lado/4, x0-lado/4, x0-lado/8], [y0+lado/4, y0+lado/2, y0+lado*3/8])
    
    setPenColor(CYAN)
    filledPolygon([x0, x0-lado/2, x0, x0+lado/2],[y0+lado/2, y0, y0-lado/2, y0])
    show()

def baldosa(x0:float, y0:float, lado:float):
    setPenColor(CYAN)
    filledSquare(x0-lado*3/8, y0+lado*3/8, lado/8)
    filledSquare(x0+lado*3/8, y0+lado*3/8, lado/8)
    filledSquare(x0+lado*3/8, y0-lado*3/8, lado/8)
    filledSquare(x0-lado*3/8, y0-lado*3/8, lado/8)
    
    setPenColor(RED)
    filledSquare(x0-lado/8, y0+lado*3/8, lado/8)
    filledSquare(x0+lado/8, y0+lado*3/8, lado/8)
    filledSquare(x0-lado/8, y0-lado*3/8, lado/8)
    filledSquare(x0+lado/8, y0-lado*3/8, lado/8)
    filledSquare(x0-lado*3/8, y0+lado/8, lado/8)
    filledSquare(x0-lado*3/8, y0-lado/8, lado/8)
    filledSquare(x0+lado*3/8, y0+lado/8, lado/8)
    filledSquare(x0+lado*3/8, y0-lado/8, lado/8)
    
    setPenColor(YELLOW)
    filledPolygon([x0-lado/2, x0-lado/4, x0-lado*3/8], [y0+lado/4, y0+lado/4, y0+lado/8])
    filledPolygon([x0-lado/2, x0-lado/4, x0-lado*3/8], [y0-lado/4, y0-lado/4, y0-lado/8])
    filledPolygon([x0-lado/4, x0-lado/4, x0-lado/8], [y0-lado/4, y0-lado/2, y0-lado*3/8])
    filledPolygon([x0+lado/4, x0+lado/4, x0+lado/8], [y0-lado/4, y0-lado/2, y0-lado*3/8])
    filledPolygon([x0+lado/4, x0+lado/2, x0+lado*3/8], [y0-lado/4, y0-lado/4, y0-lado/8])
    filledPolygon([x0+lado/4, x0+lado/2, x0+lado*3/8], [y0+lado/4, y0+lado/4, y0+lado/8])
    filledPolygon([x0+lado/4, x0+lado/4, x0+lado/8], [y0+lado/4, y0+lado/2, y0+lado*3/8])
    filledPolygon([x0-lado/4, x0-lado/4, x0-lado/8], [y0+lado/4, y0+lado/2, y0+lado*3/8])
    
    setPenColor(CYAN)
    filledPolygon([x0, x0-lado/2, x0, x0+lado/2],[y0+lado/2, y0, y0-lado/2, y0])
    
def dibujar_fila(x0:float, y0:float, lado:float, n:int):
    """
    PRE: n>= 0, lado >= 0
    
    Dibuja una fila de n baldosas de lado x lado alternando un cuadrado
    simple de color azul y una baldosa.
    El centro del cuadrado de más a la izquierda es (x0, y0) y la
    primera baldosa de la izquierda es un cuadrado simple de color azul.
  """
    setXscale(-(n*lado)/2, (n*lado)/2)
    setYscale(-(n*lado)/2, (n*lado)/2)
    for i in range (n):
        if i % 2 == 0:
            setPenColor(BLUE)
            filledSquare(x0+i*lado, y0, lado/2)
        else:
            baldosa(x0+i*lado, y0, lado)
    show()

def dibujar_suelo(x0:float, y0:float, lado:float, n:int):
    """
    PRE: n >=0, lado >=0
    
    Dibuja un suelo de n baldosas de lado x lado alternando un cuadrado simple de
    cualquier color y una baldosa.
    El centro del cuadrado de más a la izquierda es (x0,y0= y la primera baldosa
    de la izquierda es un cuarado simple de cualquier color.
  """
    setXscale(-(n*lado)/2, (n*lado)/2)
    setYscale(-(n*lado)/2, (n*lado)/2)
    for j in range (n):
        if j % 2 == 0:
            for i in range (n):
                if i % 2 == 0:
                    setPenColor(MAGENTA)
                    filledSquare(x0+i*lado, y0-j*lado, lado/2)
                else:  
                    baldosa(x0+i*lado,y0-j*lado,lado)
        else:
            for i in range (n):
                if i % 2 == 0:
                    baldosa(x0+i*lado,y0-j*lado,lado)
                else:  
                    setPenColor(MAGENTA)
                    filledSquare(x0+i*lado, y0-j*lado, lado/2)
    show()