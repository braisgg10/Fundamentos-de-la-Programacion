def es_triangular (n:int) -> bool:
    k = 1
    var = False
    while k <=n and not var:
        if suma_intervalo (1,k) == n:
            var = True
        else:
            k+= 1
    return var

def suma_intervalo (a: int, b: int) -> int:
    res = 0
    for i in range (a,b+1):
        res+=i
    return res

def texto_triangular (n : int) -> list:
    pir=[]
    i=1
    if es_triangular(n):
        while suma_intervalo (1, i) <= n:
            pir += [i * "*"]
            i += 1
    return "\n".join(pir)

def es_perfecto (n : int) -> bool:
    if suma_divisores (n) == n:
        return True
    else:
        return False
        
def suma_divisores (n : int) -> int:
    res = 0
    i = 1
    while i <n:
        if n%i==0:
            res += i
        else:
            res=res
        i += 1
    return res

def cuantos_perfectos (n : int) -> int:
    res = 0
    for i in range (1,n+1):
        if es_perfecto(i) == True:
            res += 1
    return res

def es_primo (n : int) -> bool:
    ver = True
    i = 2
    while i <= (n//2) and ver:
        if n%i == 0:
            ver = False
        else:
            i+=1
    return ver

def cuantos_primos (n : int) -> int:
    ct= 0
    for i in range (2,n+1):
        if es_primo(i) == True:
            ct+=1
    return ct

def tuplas_n_primos (n : int) -> list:
    res= []
    i = 1
    while i <= n: 
        if es_primo(i) == True:
            res = res + [(10**i, cuantos_primos(10**i))]
            i += 1
        else:
            i += 1
    return res