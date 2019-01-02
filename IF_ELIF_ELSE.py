print("Verificacion notas")

nota_alumno=int(input("Introduce tu nota, porfavor: "))

if nota_alumno<0:
	print("Nota incorrecta.")
elif nota_alumno<5: 
	print("Estas SUSPENDIDO, ya puedes estudiar paleto.")
elif nota_alumno<6: 
	print("Por los pelos, un SUFICIENTE.")
elif nota_alumno<7:
	print("No esta mal, un BIEN.")
elif nota_alumno<8:
	print("Vas bien maquina, un NOTABLE.")
elif nota_alumno<=10:
	print("Pues mira, un SOBRESALIENTE maquinoide!")
else: #per a notes superiors a 10
	print("Nota incorrecta.")

print("FIN SERAFIN")

#Només entrarà als elif si no ha entrat a algun dels anteriors, una vegada ha entrat a algun d'ells el bloc finalitza, amb un ELSE (Per finalitzar bloc IF)