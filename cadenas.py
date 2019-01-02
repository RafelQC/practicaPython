nombreUsuario=input("Introduce tu nombre de usuario: ")

print("Tú nombre es:", nombreUsuario)
print("Tú nombre es:", nombreUsuario.lower()) #todo en minusculas
print("Tú nombre es:", nombreUsuario.upper()) #todo en mayusculas
print("Tú nombre es:", nombreUsuario.capitalize()) #primera letra en mayusculas
print("Tú nombre es:", nombreUsuario.title()) #tot en minuscules excepte els incis de  paraules en majuscules
usuarioEdad=input("Introduce tú edad: ")
print(usuarioEdad.isdigit()) #booleano si es un digit o un str

while(usuarioEdad.isdigit()==False): #No sale del bucle hasta que no nos dé una edad real
	print("Error.")
	usuarioEdad=input("Vuelva a ntroducir su edad: ")

if(int(usuarioEdad)<18):
	print("No puedes pasar, eres MENOR")
else:
	print("Puedes pasar, eres MAYOR DE EDAD")