class coche():
	def desplazamiento(self):
		print("Me desplazo utilizando 4 ruedas")

class moto():
	def desplazamiento(self):
		print("Me desplazo utilizando 2 ruedas")

class camion():
	def desplazamiento(self):
		print("Me desplazo utilizando 6 ruedas")

def desplazamientoVehiculo(vehiculo): #polimorfismo, se pasa un objeto como parametro que le servira para seleccionar que "desplazamiento" tiene que seleccionar
	vehiculo.desplazamiento()

#miVehiculo=moto()
#miVehiculo.desplazamiento()

#mivehiculo2=coche()
#mivehiculo2.desplazamiento()	

#mivehiculo3=camion()
#mivehiculo3.desplazamiento()

miVehiculo=camion()
desplazamientoVehiculo(miVehiculo)