from random import *
from quotes import *

def frase_huecos (frase:list, cambios:list) -> list:
    if len(frase) > 0:
        for i in cambios:
            frase.pop(i)
            frase.insert(i,"< >")
    return frase

def frase_usuario (frase : list) -> list:
    a = []
    for i in frase:
        if i == "< >":
            p = input()
            a.append(p)
        else:
            a.append(i)
    return 

def aciertos (una:list, otra:list, cambios: list) -> int:
    ct=0
    for i in cambios:
        if una[i] == otra[i]:
            ct+=1
        else:
            ct=ct
    return ct

def lista_cambios_random(m:int, n:int) -> list:
    a = []
    while len(a) < m:
        b=randint(0,n-1)
        if b not in a:
            a.append(b)
        else:
            a=a
    return a

def acertar():
    frase_original_texto = "ser o no ser esa es la cuestion"
    frase_original = frase_original_texto.split()
    lista_cambios = lista_cambios_random(3, len(frase_original)-1)
    frase_a_rellenar = ""
    for i in range(0, len(frase_original)):
        if i in lista_cambios: #== lista_cambios[0] or i == lista_cambios[1] or i == lista_cambios[2]:
            frase_a_rellenar += " < >"
        else:
            frase_a_rellenar+= " " + frase_original[i] + " "
    frase_rellena = input(frase_a_rellenar+" -- B.Gil")
    frase_rellena=frase_rellena.split()
    acierto=0
    s = 0
    for i in range (0,len(frase_original)):
        if i in lista_cambios: #==lista_cambios[0] or i==lista_cambios[1] or i==lista_cambios[2]:
            if frase_rellena[s]==frase_original[i]:
                acierto+=1
            else:
                acierto = acierto
            s+=1
    print ("Has acertado "+str(acierto)+ "palabra/s, la frase original era: " + frase_original_texto)

def acertar_random():
    c = int(input("Dime un numero entre 2 y 6; estas serán las incógnitas de tu frase"))
    n = randint(0,len(frases)-1)
    frase_original_texto= frases[n]
    frase_original= frase_original_texto.split()
    lista_cambios = lista_cambios_random(c, len(frase_original)-1)
    frase_a_rellenar=""
    for i in range (0,len(frase_original)):
        if i in lista_cambios: #or i==lista_cambios[1] or i==lista_cambios[2] or i==lista_cambios[3] or i==lista_cambios[4] or i==lista_cambios[5]:
            frase_a_rellenar=frase_a_rellenar + " <>"
        else:
            frase_a_rellenar=frase_a_rellenar+ " " + frase_original[i]
    frase_a_rellenar= frase_a_rellenar + " "
    frase_rellena=input("Tienes que adivinar las palabras que van en los <> de la siguiente frase:  " + frase_a_rellenar + "- " + autores[n] + "  ")
    fr=frase_rellena.split()
    acierto=0
    s=0
    bien=""
    for i in range (0,len(frase_original)):
        if i in lista_cambios: #i==lista_cambios[0] or i==lista_cambios[1] or i==lista_cambios[2]:
            if fr[s]==frase_original[i]:
                acierto+=1
                if acierto==1:
                    bien = fr[s]
                else:
                    bien= bien + " y " + fr[s]
            s+=1
    while(acierto<c):
        fr = ""
        frase_rellena=input("Has acertado " + str(acierto) + " palabra/s: " + bien + ", vuelve a intentarlo  ")
        fr=frase_rellena.split()
        acierto=0
        s=0
        bien=""
        for i in range (0,len(frase_original)):
            if i in list_cambios:  #i==lista_cambios[0] or i==lista_cambios[1] or i==lista_cambios[2] or i==lista_cambios[3] or i==lista_cambios[4] or i==lista_cambios[5]:
                if fr[s]==fo[i]:
                    acierto+=1
                    if acierto==1:
                        bien = fr[s]
                    else:
                        bien= bien + " y " + fr[s]
                s+=1
    return "Has ganado, la frase era: " + frase_original_texto + "- " + autores[n] + "  "