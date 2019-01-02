for letra in "Python":
	if letra=="h":
		continue	#pasa directament a la següent iteració del bucle, parescut a BREAK pero sense sortir del bucle, a la següent iteració directament
	print("Viendo la letra "+letra)

#calculo de cuantos caracteres tiene la variable
nombre = "Pildoras Informaticas"
contador=0
for i in nombre:
	if i==" ":
		continue #continue hace que desprecie los espacios
	contador+=1
print("Sin espacios "+str(contador))
print("Con espacios "+ str(len(nombre)))

#PASS

#while True: #bucle infinito
	#pass #salir del bucle infinito

class MiClase:
	pass #Para implementar más tarde

#ELSE en bucles FOR o WHILE

email=input("Introduce el e-mail, por favor. ")
for i in email:

	if i=="@":
		arroba=True
		break; #si esta instrucción se realiza, hará que salgamos del bucle FOR y además no ejecutaremos el siguiente ELSE pues habremos interrumpido el FOR
else: #este ELSE esta referenciado al bucle FOR, solo se ejecutará despues de la ultima iteración del bucle FOR, si no se ha realizado la última por un "BREAK" por ejemplo, el ELSE no se ejecutará
	arroba=False
print(arroba)