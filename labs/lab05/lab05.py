"""
  Funciones a completar para el lab5
"""

from tiempo import Tiempo


def suma_tiempos (t1 : Tiempo, t2 : Tiempo) -> Tiempo:
    """
  POST: resultado: Un nuevo objeto Tiempo que representa la suma de 
                   los tiempos tiempo1 y tiempo2
        No altera tiempo1 ni tiempo2

  EJEMPLO: 
    suma_tiempos(Tiempo(1,59), Tiempo(1,2)) -->  Tiempo(3,1)
    """
    horas = t1.horas + t2.horas
    minutos = t1.minutos + t2.minutos
    if minutos >= 60:
        horas += minutos // 60 
        minutos = minutos % 60
    return Tiempo(horas, minutos)