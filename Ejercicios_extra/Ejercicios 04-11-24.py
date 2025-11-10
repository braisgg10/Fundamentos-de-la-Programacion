#1
def suma (x:list) -> int:
	res=0
	for e in x:
		res += e
	return res

#2
def input_lista_str() -> list:
	n = int(input("Dime cuantos elementos quieres que tenga tu lista"))
	lista = []
	for i in range (n):
		x = int(input("Dime que elemento quieres que añada a la lista"))
		lista = lista + [i]
	return lista

#3
def input_lista_str() -> list:
	n = int(input("Dime cuantos números quieres que tenga tu lista"))
	lista = []
	for i in range (n):
		x = int(input("Dime que numero quieres que añada a la lista"))
		lista = lista + [i]
	return lista

#4
def suma_pares (x:list) -> int:
	res = 0
	for e in x:
		if e % 2 == 0:
			res += e
		else: 
			res = res
	return res

#5
def veces_en_lista (x:list) -> int:
	ct=0
	n = int(input("Dime el elemento que quieres que cuente en tu lista"))
	for i in x:
		if i == n:
			ct += 1
		else:
			ct = ct
	return ct

#6
def max_longitud(x:list) -> str:
	res = len(lista[0])
	for i in x[1:]:
		res = max (len(palabra), res)
	return res

#7
def palabra_max_longitud (x:list) -> str:
	res = lista[0]
	for i in x[1:]:
		res = max_palabra(palabra, res)
	return res
	
def max_palabra(una:str, otra:str) -> str:
	if len(una)>= len(otra):
		return una
	else:
		return otra
	
#8
def lista_pares(x:list) -> list:
	y = []
	for i in x:
		if i %2 == 0:
			y += str(i)
		else:
			y = y
	return y

#9
def incremento(x:list)->list:
    for i in range(len(x)):
        x[i] += 1
    return x

#10
def incrementar (lista:list):
    for i in range(len(lista)):
        lista [i] += 1
        