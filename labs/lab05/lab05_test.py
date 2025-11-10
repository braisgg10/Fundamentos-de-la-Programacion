"""
  Tester de lab05
"""

from tiempo import Tiempo
import lab05

def test_suma_tiempos ():
  print("Ejecutando test_suma_tiempos")
  t1 = Tiempo(1, 59)
  t2 = Tiempo(1, 2)
  res1 = lab05.suma_tiempos(t1, t2)
  print(res1.horas == 3 and res1.minutos == 1)

  t1 = Tiempo(1, 59)
  t2 = Tiempo(3, 59)
  res1 = lab05.suma_tiempos(t1, t2)
  print(res1.horas == 5 and res1.minutos == 58)

  t1 = Tiempo(1, 50)
  t2 = Tiempo(0, 2)
  res1 = lab05.suma_tiempos(t1, t2)
  print(res1.horas == 1 and res1.minutos == 52)

test_suma_tiempos()
