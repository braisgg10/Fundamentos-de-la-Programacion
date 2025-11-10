def guionizador_par (a: str) -> str:
    return a[:int(len(a))//2] + "-" + a[int(len(a))//2:]
    
def guionizador_impar (b: str) -> str:
    return b[:int(len(b))//2] + "-" + b[int(len(b)//2):(len(b)//2+1)] + "-" + b[int(len(b)//2+1):]