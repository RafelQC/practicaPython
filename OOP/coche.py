class coche():

	def __init__(self): #CONSTRUCTOR definimos los estados iniciales de los objetos creados, más adelante pueden ser modificados
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4  #con las "__" no se pueden modificar estas variables desde fuera del objeto (ENCAPSULADO)
		self.__enmarcha=False

	def arrancaFrena(self,arrancamos):
		self.__enmarcha=arrancamos

		if(self.__enmarcha):
			chequeo=self.__chequeoInterno()
		
		if(self.__enmarcha and chequeo):
			return "El coche está en marcha. "

		elif(self.__enmarcha and chequeo==False):
			return "Algo ha ido mal en el chequeo, no podemos arrancar."

		else:
			return "El coche está parado. "

	def estado(self):
		print("El coche tiene ", self.__ruedas, "ruedas, ", "un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

	def __chequeoInterno(self): #aquest metode esta encapsulat, només es pot cridar dins l'objecte
		print("Realizando chequeo interno... ")

		self.gasolina="ok"
		self.aceite="bajo"
		self.puertas="cerradas"

		if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
			return True
		else:
			return False


miCoche=coche()

#print(miCoche.largoChasis)
#print(miCoche.ruedas)

print(miCoche.arrancaFrena(True))
miCoche.estado()

print(" - - - - -  A continuación creamos el segundo objeto...  - - - - -")

miCoche2=coche()
print(miCoche2.arrancaFrena(False))
miCoche2.ruedas=2
miCoche2.estado()

