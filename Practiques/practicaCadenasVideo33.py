def correoArrobaOk(correo):

	if(correo.count("@")==1 and correo.find("@")>0 and correo.find("@")<(len(correo)-1)):
		return "Dirección de correo correcta"
	else:
		return "Dirección de correo ERRONEA"

miCorreo=input("Introduzca su dirección de correo electrónico: ")

print(correoArrobaOk(miCorreo))

#print(miCorreo.find("@")) #indica en que posición esta el primer caracter seleccionado
#print(len(miCorreo))      #indica la longitud de la cadena