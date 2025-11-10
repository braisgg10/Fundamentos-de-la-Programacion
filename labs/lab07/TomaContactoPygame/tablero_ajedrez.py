from stddraw import *
from color import Color

def dibujar_fila (x0 : float, y0 : float, lado : float, \
  n : int, c1 : Color, c2 : Color):
    setXscale(-(n*lado)/2, (n*lado)/2)
    setYscale(-(n*lado)/2, (n*lado)/2)
    
    for i in range (n):
        if i % 2 == 0:
            setPenColor(c1)
        else:  
            setPenColor(c2)
        filledSquare(x0+i*lado, y0, lado/2)
    show()

def dibujar_tablero (x0 : float, y0 : float, lado : int, \
  n : int, c1 : Color, c2 : Color):
    setXscale(-(n*lado)/2, (n*lado)/2)
    setYscale(-(n*lado)/2, (n*lado)/2)
    for j in range (n):
        if j % 2 == 0:
            for i in range (n):
                if i % 2 == 0:
                    setPenColor(c1)
                else:  
                    setPenColor(c2)
                filledSquare(x0+i*lado, y0-j*lado, lado/2)
        else:
            for i in range (n):
                if i % 2 == 0:
                    setPenColor(c2)
                else:  
                    setPenColor(c1)
                filledSquare(x0+i*lado, y0-j*lado, lado/2)
        filledSquare(x0, y0-j*lado, lado/2)
    show()