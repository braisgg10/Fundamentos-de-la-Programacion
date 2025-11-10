from tiempo import Tiempo

t = Tiempo(2,30)

s = t
t.minutos = 20
print("t.minutos is: " + str(t.minutos))
print("s.minutos is: " + str(s.minutos) + '\n')

s = Tiempo(t.horas, t.minutos)
print("t.minutos is: " + str(t.minutos))
print("s.minutos is: " + str(s.minutos) + '\n')

t.minutos = 10
print("t.minutos is: " + str(t.minutos))
print("s.minutos is: " + str(s.minutos))