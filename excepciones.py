def divide():
	try: #es fica dins el try totes aquelles operacions que són subsceptibles de tenir errors dintre
		op1=(float(input("Inserta el primer número: ")))
		op2=(float(input("Inserta el segundo número: ")))

		print("La división da como resultado: "+str(op1/op2))

	except ValueError: #només s'executaran aquestes lines de codi si s'ha produit l'error remarcat "ValueError"

		print("El valor introducido no es correcto. ")

	except ZeroDivisionError:

		print("No se puede dividir por cero. ")

	finally: #sempre s'executaran aquestes lines de còdi pasi el que pasi anteriorment

		print("Cálculo finalizado. ")

#divide()


#RAISE nosotros lanzamos nuestras excepciones para manejar errores de logica de nuestro programa (pero que no son errores de programación)

def evaluaEdad(edad):
	if edad<0:
		raise TypeError("Esta edad no es real. ") #lanzamos nuestro error


	if edad<20:
		return "Eres demasiado joven. "
	elif edad<40:
		return "Eres joven. "
	elif edad<65:
		return "Eres maduro. "
	elif edad<100:
		return "Cuidate... "

#print(evaluaEdad(-4))

import math #libreria de operaciones matematicas

def calculaRaiz(num1):

	if num1<0:
		raise ValueError("EL numero no puede ser negativo. ") #lanzamos nuestro error

	else:
		return math.sqrt(num1)

op1=(int(input("Introduce un numero para la raiz cuadrada: ")))

try:
	print(calculaRaiz(op1))

except ValueError as ErrorNumeroNegativo:

	print(ErrorNumeroNegativo)


print("Programa finalizado. ")