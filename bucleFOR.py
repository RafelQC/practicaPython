for i in [1,2,3]: #recorre la lista utilizando el for hasta que no haya mas valores
	print("Hola")
for i in [1,2,3]:
	print(i)
for estaciones in ["verano", "otoño", "primavera", "invierno"]:
	print (estaciones)

for i in [1,2,3]:
	print("Hola ", end="") #end="" hace que no haya salto de linea con el siguiente print
print("")
print("Fin programa")

contador=0
email=False
for i in "juan@pildorasinformativas.com": #recorre todo el string letra a letra
	print(i, end="")
	if (i=="@" or i=="."):
		contador+=1
print("")
if contador==2:
	email=True

if email:
	print("El correo es correcto.")
else:
	print("El correo es incorrecto")

#RANGE

for i in range(5):  #amb la funció RANGE es fa un FOR de la manera usual
	print(i)

for i in range(5):
	print(f"Valor de la variable {i}") #concatenacion de una cadena string con una variable INT mediante la función f

for i in range(1,6): #empieza por el 1 acabando por el 5
	print(f"Valor de la variable {i}")

for i in range(0,16,5): #empieza por el 0 acabando por el 15 de 5 en 5
	print(f"Valor de la variable {i}")

valido = False

email=input("Introduce tu e-mail: ")

for i in range(len(email)):
	if email[i]=="@":
		valido = True

if valido == True:
	print("El a-mail es correcto.")
else:
	print("El e-mail es INCORRECTO.")