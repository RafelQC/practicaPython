print("Programa Becas 2019:")

distancia_escuela=int(input("Introduce la distancia de casa a la escuela: "))
numero_hermanos=int(input("Introduce el numero de hermanos en la familia: "))
salario_familiar=int(input("Introduce el salario total familiar: "))

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<20000:
	print("Tiene derecho a beca.")
else:
	print("No tiene derecho a beca.")

print("Fin programa becas")

