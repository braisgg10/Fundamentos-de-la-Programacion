# ahorcado.py

"""
  Estado del ahorcado
"""  

def mostrar_estado (fallos : int):              
	"""
  Imprime el estado del ahorcado segun los fallos hasta llegar a 
        ____
       |    |
       |  __0__
       |    |
       |   / \
    ___|____
    
  """
	if fallos == 0:
		print("    ____    ")
		print("   |    |   ")
		print("   |        ")
		print("   |        ")
		print("   |        ")
		print("___|____    ")		
	elif fallos == 1:
		print("    ____    ")
		print("   |    |   ")
		print("   |    0   ")
		print("   |        ")
		print("   |        ")
		print("___|____    ")		
	elif fallos == 2:
		print("    ____    ")
		print("   |    |   ")
		print("   |  __0   ")
		print("   |        ")
		print("   |        ")
		print("___|____    ")		
	elif fallos == 3:
		print("    ____    ")
		print("   |    |   ")
		print("   |  __0__ ")
		print("   |        ")
		print("   |        ")
		print("___|____    ")		
	elif fallos == 4:
		print("    ____    ")
		print("   |    |   ")
		print("   |  __0__ ")
		print("   |    |   ")
		print("   |        ")
		print("___|____    ")		
	elif fallos == 5:
		print("    ____    ")
		print("   |    |   ")
		print("   |  __0__ ")
		print("   |    |   ")
		print("   |   /    ")
		print("___|____    ")	
	else: #fallos == 6:
		print("    ____    ")
		print("   |    |   ")
		print("   |  __0__ ")
		print("   |    |   ")
		print("   |   / \  ")
		print("___|____    ")			
  
# mostrar_estado(6)

