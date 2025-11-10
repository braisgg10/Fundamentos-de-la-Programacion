def sustitucion (lista : list, una : str, otra : str) -> list:
    resultado = []
    for i in lista:
        if i == una:
            resultado.append(otra)
        else:
            resultado.append (i)
    return resultado

def sustituir (lista:list, una:str, otra:str):
    for i in range (len(lista)):
        if lista [i]==una:
            lista[i]=otra
    

    # a = []
    # for i in lista:
        # if i == una:
            # a.append (otra)
        # else:
            # a.append (i)
    # lista = a
	
	
def aciertos (una:list, otra: list, cambios:list) -> int:
    aciertos = 0
    for i in cambios:
        if una[i] == otra[i]:
            aciertos += 1
        else:
            aciertos = aciertos
    return aciertos


VOCALES_MIN = ["a", "e", "i", "o", "u"]
def es_vocal (c : str) -> bool:
    return c in VOCALES_MIN
    # if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        # return True
    # else:
        # return False


def cambio_vocales (palabra : str, car : str) -> str:
    res = ""
    for i in palabra:
        if es_vocal(i) == True:
            res += car
        else:
            res+=i
    return res
    
    # palabra = palabra.split()
    # for i in palabra:
        # if es_vocal(i) == True:
            # palabra.append (car)
        # else:
            # palabra.append (i)
    # palabra = palabra.join()
    # return palabra
    
def paletot (frase : list, car : str) -> list:
    res = []
    for palabra in frase:
        res += [cambio_vocales(palabra, car)]
    return res
    
    # a=frase.split()
    # d=[]
    # c=[]
    # for j in a:
        # b=j.split()
        # for i in b:
            # if es_vocal(i) == True:
                # d.append (car)
            # else:
                # d.append (i)
        # d.join()
        # c.append(d)
    # return c