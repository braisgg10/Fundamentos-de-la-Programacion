# ahorcado.py

"""
  Estado del ahorcado
"""  

def mostrar_estado(fallos: int):              
    """
    Imprime el estado del ahorcado según los fallos hasta llegar a:
        ____
       |    |
       |  __0__
       |    |
       |   / \
    ___|____
    """
    estados = [
        # 1
        """
        ____
       |    |
       |  
       |    
       |   
    ___|____ 
        """,
        # 2
        """
        ____
       |    |
       |    0
       |    
       |   
    ___|____
        """,
        # 3
        """
        ____
       |    |
       |  __0
       |    
       |   
    ___|____
        """,
        # 4
        """
        ____
       |    |
       |  __0__
       |    
       |   
    ___|____
        """,
        # 5
        """
        ____
       |    |
       |  __0__
       |    |
       |   
    ___|____
        """,
        # 6
        """
        ____
       |    |
       |  __0__
       |    |
       |   / 
    ___|____
        """,
        # 7
        """
        ____
       |    |
       |  __0__
       |    |
       |   / \
    ___|____
        """
    ]
    print(estados[min(fallos, len(estados) - 1)])