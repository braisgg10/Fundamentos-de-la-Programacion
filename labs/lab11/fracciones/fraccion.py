from math import gcd

class Fraccion:
    def __init__(self,num,den):
        if den == 0:
            raise ValueError("El denominador no puede ser cero")
        self.num=num
        self.den=den
        self.simplificar()
    
    def simplificar(self):
        mcd=gcd(self.num,self.den)
        self.num //= mcd
        self.den //= mcd
        if self.den<0:
            self.den=-self.den
            self.num=-self.num
        f=(self.num,self.den)    
        return f  
           
    def __str__(self):
        respuesta=str(self.num)+"/"+str(self.den)
        if self.den!=1:
            return respuesta
        else:
            return str(self.num)
    
    def __eq__(self,otra):
        return self.simplificar()==otra.simplificar()
        
        
    def __add__(self,otra):
        den2=self.den*otra.den
        num2=self.num*otra.den+otra.num*self.den
        return Fraccion (num2,den2)
        
    
    def __sub__ (self,otra):
        den2=self.den*otra.den
        num2=self.num*otra.den-otra.num*self.den
        return Fraccion (num2, den2)
    
    def __mul__(self,otra):
        den2=self.den*otra.den
        num2=self.num*otra.num
        return Fraccion (num2, den2)
    
    def __truediv__(self,otra):
        if otra.num == 0:
            raise ZeroDivisionError("No se puede dividir por una fracción con numerador cero.")
        den2=self.den*otra.num
        num2=self.num*otra.den
        return Fraccion (num2, den2)

    def to_string (fracciones : list) -> str:
        lista_str = []
        for i in fracciones:
            lista_str += [str(i)]
        return f"[{', '.join(lista_str)}]"
        # texto="["
        # for i in fracciones:
            # if fracciones[i] == fracciones [-1]:
                # texto += "(" + str(i) + ") "
            # else:
                # texto += "(" + str(i) + "), "
        # texto += "]"
        # return texto   
        
    def suma_serie(n:int):
        res = Fraccion (1,1)
        for i in range (2,n+1):
            res += Fraccion (1,i)
        return res
    
    def simplificadas (fracciones : list) -> list:
        lista=[]
        for i in fracciones:
            f=i.simp()
            lista.append(f)
        return lista

        