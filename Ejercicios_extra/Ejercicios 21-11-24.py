class Punto:
    def __init__ (self, x:float, y:float):
            self.x = x
            self.y = y

class Personaje:
    num_personajes = 0
    
    def __init__ (self, nombre:str, ciudad:str, puntos:int):
        self.nombre = nombre
        self.ciudad = ciudad
        self.puntos = puntos
        Personaje.num_personajes += 1
         
    def __str__ (self) -> str:
        return "(" + self.nombre + ", " + self.ciudad + ", " + \
               str(self.puntos) + ")"
    def saludar (self):
        print("Hola, soy " + self.nombre + " de " + self.ciudad)


import stddraw
class Hora:
  """
  PRE: () -> Hora
  POST: resultado: la Hora ahora
  """
    def __init__ (self, hh: int, mm: int, ss: int):
        self.hh = hh
        self.mm = mm
        self.ss = ss
    
    def ahora ():
        ahora = datetime.now()
        return Hora(ahora.hour, ahora.minute, ahora.second)
        
    def reloj ():
        while True:
            clear (GRAY)
            text (0,0,str(Hora.ahora())
            show (1000)
    def temporizador (final: Hora):
        h = final
        while not h.es_menor(Hora(0,0,0)):
            clear(GRAY)
            text (0,0,str(h))
            show(1000)
            h.restar(Hora(0,0,1))
        text(0,0,Hora(0,0,0))
        show()
        
    def es_menor(self):
    def restar(self):
# hora = Hora(12,23,57)