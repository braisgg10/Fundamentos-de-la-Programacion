# fraccion_menu.py

from fraccion import *
from menu import *
  
PRIMER_OPERANDO  = "1" 
SEGUNDO_OPERANDO = "2" 
SUMA             = "3" 
RESTA            = "4" 
PRODUCTO         = "5" 
DIVISION         = "6" 
SALIR            = "7" 

f1=None
f2=None

def lectura (fraccion: str) -> Fraccion:
  """
  POST: resultado: Fraccion leída del input con formato: "a/b"
  """
  f = input(f"{fraccion} > ")
  l_f = f.split("/")
  n_f = int(l_f[0])
  d_f =int(l_f[1])
  return Fraccion (n_f, d_f)
  
    
def calculadora (op : str):
  """
  Realiza la operación correspondiente de la calculadora:
    op = PRIMER_OPERANDO  --> leer f1
    op = SEGUNDO_OPERANDO --> leer f2
    op = SUMA             --> calcular f1 + f2
    op = RESTA            --> calcular f1 - f2
    op = PRODUCTO         --> calcular f1 * f2
    op = DIVISION         --> calcular f1 / f2
    op = SALIR            --> fin = True
  
  PAUTA: 
    Declarar:
      global fin
      global f1
      global f2 
  
  """
  global fin
  global f1
  global f2
  
  if op == "1":
    f1 = lectura("Fracción 1")
    print (f"Fraccion 1: {f1}")
  
  elif op == "2":
    f2 = lectura("Fraccion 2")
    print (f"Fraccion 2: {f2}")
  
  elif op == "3":
    if f1 is not None and f2 is not None:
      print(f" {f1} + {f2} = {f1+f2}")
    else: 
      print("Asegurate de tener ambos operandos antes de realizar alguna operación")
  
  elif op == "4":
    if f1 is not None and f2 is not None:
      print(f" {f1} - {f2} = {f1-f2}")
    else: 
      print("Asegurate de tener ambos operandos antes de realizar alguna operación")
  
  elif op == "5":
    if f1 is not None and f2 is not None:
      print(f" {f1} * {f2} = {f1*f2}")
    else: 
      print("Asegurate de tener ambos operandos antes de realizar alguna operación")
  
  elif op == "6":
    if f1 is not None and f2 is not None:
      print(f" {f1} / {f2} = {f1/f2}")
    else: 
      print("Asegurate de tener ambos operandos antes de realizar alguna operación")
  
  elif op == "7":
      fin = True
      print ("Saliendo de la calculadora...")
  else:
      print("Operación no reconocida")
  
    
def operar (menu : Menu):
  """
  Presenta las opciones del menú.
  Lee la opción elegida por el usuario.
  Realiza la operación correspondiente de la calculadora.
  """
  global fin
  fin = False
  while not fin: 
    menu.mostrar_opciones()
    op = menu.leer_opcion()
    calculadora(op)
    
opciones = ["Primer operando", "Segundo operando", "Suma", "Resta", 
            "Producto", "Division", "Salir"]
menu = Menu(opciones)
operar(menu)
