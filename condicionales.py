#edad=int(input("Introduce la edad: "))

#if 0<edad<100:
	#print("La edad es correcta")
#else:
	#print("La edad es incorrecta")
#print(" "); print(" "); print(" ")

salario_presidente=int(input("Introduce el salario del presi: "))
print("El salario del presi es: "+str(salario_presidente)) #concatenar cadenas (transformando un ENTERO en un STRING)

salario_gerente=int(input("Introduce el salario del gerente: "))
print("El salario del gerente es: "+str(salario_gerente))

salario_jefeseccion=int(input("Introduce el salario del jefe de sección: "))
print("El salario del jefe de seción es: "+str(salario_jefeseccion))

salario_admin=int(input("Introduce el salario del administrativo: "))
print("El salario del administrativo es: "+str(salario_admin)) 


if salario_admin<salario_jefeseccion<salario_gerente<salario_presidente:
	print("Los salarios son correctos.")
else:
	print("Los salarios son incorrectos, debemos revisarlo, VAMOS VAMOS!!!")