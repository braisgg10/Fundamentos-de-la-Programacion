def media(a:float, b:float) -> float:
	"""
	 POST:resultado:la media entre a y b
	"""
	return(a+b)/2
	

x=float(input("Primer número>"))
y=float(input("Segundo número>"))

print("Media de " + str(x) + " y " + str(y) + " = " + str(media(x,y)))