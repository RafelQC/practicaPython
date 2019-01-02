import math #definicion de clase math para poder usar sus funciones

edad=int(input("Introduce la edad: "))

contador=1
while (edad<0 or edad>100) and contador<6:
	contador+=1
	print("Error al introducir la edad")
	edad=int(input("Vuelva a introducir la edad: "))
	if contador==5:
		print("Último intento antes de finalizar.")

if contador==6:
	print("No hemos podido verificar su edad")
else:
	print(f"Gracias, la edad introducida ha sido de {edad} años")

#IMPORTACION

print("Programa de calculo de la raiz cuadrada.")

numero=int(input("Introduce el numero. "))

intentos=0
while numero<0:
	print("No se puede hallar la raiz cuadrada de un numero negativo.")
	
	if intentos==2:
		print("Has consumido demasiados intentos.")
		break; #sale del bucle while
	numero=int(input("Introduce el numero. "))
	if numero<0:
		intentos+=1
if intentos<2:
	solucion=math.sqrt(numero) #uso de la calse math para poder realizar la raiz cuadrada
	print(f"La raiz cuadrada de {numero} es {solucion}")