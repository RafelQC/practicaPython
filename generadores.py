#generar numeros pares con una funcion ESTANDAR
def generaPares(limite):

	num=1
	miLista=[]

	while num<=limite:

		miLista.append(num*2)
		num=num+1

	return miLista #realiza todas las iteraciones necesarias y te devuelve todo el carro de pares con el limite establecido posteriormente (limite)

print(generaPares(10))

#generar numeros pares con un GENERADOR

def generaPares(limite):

	num=1

	while num<=limite:

		yield num*2 #guardamos el dato como si fuera un RETURN y salimos de la función dejandola en STANDBY, pero sin un NEXT este STANDBY no va a funcionar
		num=num+1

devuelvePares=generaPares(10)

for i in devuelvePares:
	print(i)

#aplicamos NEXT al GENERADOR

def generaParesSinlimite():

	num=2
	while True:
		yield num #guardamos el dato como si fuera un RETURN y salimos de la función dejandola en STANDBY, pero sin un NEXT este STANDBY no va a funcionar
		num=num+2

devuelvePares=generaParesSinlimite()

print("PAR")
print(next(devuelvePares)) #usamos el NEXT para demandarle la información que tiene en STANDBY el GENERADOR
print("PAR")
print(next(devuelvePares))
print("PAR")
print(next(devuelvePares))