#acceder a SUBELEMENTOS de un elemento devuelto por un GENERADOR

def devuelve_ciudades(*ciudades): #arterisco delante del argumento de una funcion significa que va a recibir un numero indeterminado de elementos 1,2,7.. en forma de tupla
	for elemento in ciudades:
		for subElemento in elemento:
			yield subElemento

ciudadDevueltas=devuelve_ciudades("Madrid", "Barcelona", "Palma", "Ourense", "Valencia", "Bilbao")

print(next(ciudadDevueltas))
print(next(ciudadDevueltas))

#acceder a SUBELEMENTOS de un elemento devuelto por un GENERADOR utilitzando YIELD FROM

def devuelve_ciudades(*ciudades): #arterisco delante del argumento de una funcion significa que va a recibir un numero indeterminado de elementos 1,2,7.. en forma de tupla
	for elemento in ciudades:
		yield from elemento

ciudadDevueltas=devuelve_ciudades("Madrid", "Barcelona", "Palma", "Ourense", "Valencia", "Bilbao")

print(next(ciudadDevueltas))
print(next(ciudadDevueltas))