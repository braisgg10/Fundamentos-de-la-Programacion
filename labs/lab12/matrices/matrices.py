# matrices.py

""" 
  Manejo de arrays 2D
"""

# def to_string (m : list) -> str:
  # """
  # PRE: list[list[int]] -> str
  # """
  # res = ""
  # for ef in m:
    # for ec in ef:
      # res += " " + str(ec) 
    # res += "\n"  
  # return res

def to_string (m : list) -> str:
  """
  PRE: list[list[int]] -> str
  """
  res = ""                                                                                                                                                                                                                                                                                                                                                                                                                                                  
  for i in range(len(m)):
    for j in range(len(m[i])):
      res += " " + str(m[i][j]) 
    res += "\n"  
  return res
  
def suma (m : list) -> int:
  """
  PRE: list[list[int]] -> str
  POST: resultado: la suma de los elementos en m
  EJEMPLOS:
    suma([[1, 2], [3, 4]]) -> 10
    suma([[2, 2], [1, 1]]) -> 6
  """
  res = 0
  for i in range(len(m)):
    for j in range(len(m[i])):
      res += m[i][j] 
  return res

def crea_2D (fils : int, cols : int, valor : int=None):
  """
  PRE: fils >= 0, cols >= 0
  POST: resultado: una nueva matriz con fils filas y cols columnas,
                   con todos sus elementos inicializados a valor
  """
  m = [valor] * fils
  for i in range(fils):
    m[i] = [valor] * cols
  return m
  
def identidad (n : int) -> list:
  """
  PRE: int -> list[list[int]], n >= 0
  POST: resultado: la matriz identidad de tamaño n, es decir, una
                   matriz n * n con unos en la diagonal y ceros en el resto
  EJEMPLOS:
    identidad(0) ->  // matriz vacía []
    identidad(1) -> 1
    identidad(3) -> 1 0 0
                    0 1 0
                    0 0 1
  """
  res = crea_2D(n, n, 0)
  for i in range(n):
    res[i][i] = 1
  return res
 
def suma_matrices (m1 : list, m2 : list) -> list:
  """
  PRE: (list[list[int]], list[list[int]]) -> list[list[int]]
        m1 y m2 son del mismo tamaño
  POST: resultado: una nueva matriz donde cada elemento en la fila
                   i y columna j es la suma de los elementos de la fila i y 
                   columna j de m1 y m2
  EJEMPLOS:
    suma([[1,2], [3,4]], [[1,1], [2,2]]) -> [[2,3], [5,6]]
  """
  m3 = []
  f = []
  for i in range (len(m1)):
    for j in range (len(m1[i])):
      a =m1[i][j] + m2[i][j]
      f.append(a)
    m3.append(f)
    f = []
  return m3
  
def equals (m1 : list, m2 : list) -> bool:
  """
  PRE: (list[list[int]], list[list[int]]) -> bool
  POST: resultado: m1 y m2 tienen los mismos elementos y en el 
                   mismo orden
  EJEMPLOS:
    equals([[1,2], [3,4]], [[1,1], [2,2]]) --> false
    equals([[1,2], [3,4]], [[1,2], [3,4]]) --> true
  """
  e = True
  for i in range (len(m1)):
    for j in range (len(m1[i])):
      if m1[i][j] != m2[i][j]:
          e = False
  return e
  
def esta (n : int, m : list) -> bool:
  """
  PRE: (list[list[int]], int) -> bool
  POST: resultado: n está en m
  EJEMPLOS:
    esta(3, [[1,2], [3,4]]) --> true
    esta(5, [[1,2], [3,4]]) --> false  
  """
  e = False
  for i in range (len(m)):
    for j in range (len(m[i])):
      if m[i][j] == n:
          e = True
  return e 

def iguales (n : int, m : list) -> bool:
  """
  PRE: (list[list[int]], int) -> bool
  POST: resultado: todos los elementos de m son iguales a n
  EJEMPLOS:
    iguales(3, [[3,3], [3,3]]) --> true
    iguales(5, [[1,2], [3,4]]) --> false  
  """
  e = True
  i = 0
  j = 0
  while i < len(m) and e:
    while j < len(m[i]) and e:
      if m[i][j] != n:
        e = False
      else:
        j+=1
    j = 0
    i += 1
  return e
         
# m = [[1 ,2 ,3] ,[4 ,5 ,6] ,[7 ,8 ,9]]
# print(m)  
# print(to_string(m))  
# print(suma(m))  
#print(crea_2D(0, 0))
#print(crea_2D(3, 3, 3))  
#print(to_string(crea_2D(0, 0)))
# print(to_string(crea_2D(3, 3)))
# m2 = [[1 ,1 ,1] ,[1 ,1 ,1] ,[1 ,1 ,1]]
# print(to_string(suma_matrices(m, m2)))  
