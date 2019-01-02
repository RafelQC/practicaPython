frase = "hola mira que mal me va sola" #guardar string
print (frase) #imprimir variable string
print("hola, mira que bien me va sola") #imprimir caracters directament
numero = 3 #variables
peque = 2
n = type (numero) #tipo de variable, pensa que python canvia el tipo de variable segons el contingut
print (n) #imprimir variables
s = type (n)
print (s)
asignatura=opcion.lower() #convierte una cadena de string TODA en minusculas
asignatura=opcion.upper() #convierte una cadena de strins TODA en mayuscula

#nota=input("Introduce la nota del alumno:") #manera de fer una entrada per teclat, ATENCIÓ! Totes les entrades inclus numeros SON STRINGS, convertirlos mitjançant funció int()
#int(nota)    #Converteix un valor a NUMERIC tipo ENTERO
nota=int(input("Introduce la nota del alumno:"))
print("Nota és un ", type(nota))

def mensaje(numero1): #això és una funció
	while numero1 >= 1:
		print ("capullo", numero1)
		numero1 -= 1 #decrement de 1 en 1, increment (+=)

def suma(num1, num2):
	resultado=num1+num2
	return resultado #return un valor a la funció suma en aquest cas

print (suma (5,1)) #imprimir el valor de la funció suma (return resultado)

mensaje(numero) #executar funció abans definida
mensaje(peque)

#LISTAS (Arrays)

lista = ["Maria", "Marta", "Pepe", "Antonio", "Sofia"]
lista.append("Sandra") #agregar un element al final de la llista
lista.insert (2,"Bernardo") #instar un valor sense modificar altres a una posició de la llista
lista.extend (["Miguel", "Samuel", "Pepe", "Snape", "Gorosabel"]) #agrega diversos valors a una llista al final
lista.remove ("Sofia") #eliminar l'element que volguem eliminar
lista.pop() #eliminar darrer element de la llista

print ("Impresión de la lista: ", lista [:]) #accedir a tota la llista
print ("Impresión de la lista: ", lista [3]) #accedir a una posició
print ("Impresión de la lista: ", lista [0:3]) #accedir a una porció de la llista; esquerra incluit, dreta NO incluit
print ("Impresión de la lista: ", lista [:3]) #accedir tots els valors inicials fins el valor 3 NO incluit
print ("Impresión de la lista: ", lista [2:]) #accedir tots els valors començant pel valor 2 fins el final
print ("Impresión de la lista: ", lista.index ("Pepe")) #cercar la referencia dins la lista del valor "Pepe" si hi ha diversos valors iguals només ens dirà el primer
print ("Impresión de la lista: ", "Pepe" in lista) #cercar si existeix un valor, retorna un true o false
print ("Impresión de la lista: ", "Sofia" in lista) #cercar si existeix un valor, retorna un true o false

lista2 = ["Sara", "Patri", "Marina"]*3 #repetidor de listas
lista3 = ["Mar", "Sandra", "Cris", "Ana"]
lista3 = lista3 [:]*3 #repetidor de listas

milista3 = lista2+lista3 #concatenar llistes o sumar llistes
print("Listas repetidas y sumadas :" ,milista3[:])


#TUPLAS (són arrays o llistes invariables, inmodificables)	

mitupla = ("Rafel", "Quetglas", "Coll") 
print (mitupla[1]) #accedir valor tupla
tuplatolista = list(mitupla) #guardar els valor d'una tupla a una llista

milista = ["Marta", "Quetglas", "Coll", "Rafel", "Quetglas", "Coll"]
listatotupla = tuple(milista) #gaurdar una llista a una tupla
print ("Esta en la tupla?:", "Coll" in listatotupla) #comprobar si hi ha algun valor dins la tupla
print ("Quants valors hi ha com aquest? ~ ",listatotupla.count("Coll")) #numero de valor cercat que hi ha a la tupla
print (len(listatotupla)) #quina longitud és la tupla
print ("Buscar en tupla: ", listatotupla.index ("Rafel")) #cercar la referencia dins la tupla del valor "Pepe" si hi ha diversos valors iguals només ens dirà el primer

tuplaunit = ("Rafel",) #definir tupla unitaria (només te un valor)

mitupla2 = ("Rafel", 1, 9, 1988)
nom, dia, mes, agno = mitupla2 #desempaquetado de tupla, asignar els valors a les variables per ordre
print (agno)

#DICCIONARIOS

midiccionario = {"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "Portugal":"Lisboa"} #Asignar claves y valores
print(midiccionario["Francia"]) #acceder a los valores mediante las claves
midiccionario["Italia"]="Lisboa"
print(midiccionario)
midiccionario["Italia"]="Roma" #Sobreescribir las claves:valores
print(midiccionario)
del midiccionario["Reino Unido"] #eliminar clave:valores
print(midiccionario)

tuplapaises = ("Inglaterra", "Francia", "Portugal", "Alemania", "Grecia", 1988)
diccionariopaises = {tuplapaises[0]:"Londres", tuplapaises[1]:"París", tuplapaises[2]:"Lisboa", tuplapaises[3]:"Berlín", tuplapaises[4]:"Gracia", tuplapaises[5]:"S'any que vaig neixer"} #asignar valors desde una tupla
print (diccionariopaises[1988])
print(diccionariopaises.keys()) #accedeix a totes les claus
print(diccionariopaises.values()) #accedeix a tots els valors
print(len(diccionariopaises)) #quants clave:valors hi ha

#CONDICIONALES

print("Verificación de acceso:")
edad_usuario=int(input("Introduce tu edad, por favor: "))

if 	edad_usuario < 18:
	print("No puedes pasar")
else:
	print("Puedes pasar")


