class persona():

	def __init__(self, nombre, edad, residencia):
		self.nombre=nombre
		self.edad=edad
		self.residencia=residencia

	def descripcion(self):
		print("Nombre:", self.nombre, "\nEdad:", self.edad, "\nResidencia:", self.residencia)


class empleado(persona):

	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

		super().__init__(nombre_empleado, edad_empleado, residencia_empleado) #se llama al constructor de la clase padre para sus valores inciales de PERSONA
		self.salario=salario
		self.antiguedad=antiguedad

	def descripcion(self):
		super().descripcion()
		print("Salario:" , self.salario,"€ " " Antigüedad:", self.antiguedad, "años")

RafelQuetglas=persona("Rafel Quetglas", 30, "Palma")

TomeuRiera=empleado(1600, 4, "Tomeu Riera", 55, "Inca")
TomeuRiera.descripcion()

print(isinstance(TomeuRiera, persona)) #isinstance nos devuelve TRUE si TomeuRiera pertenece a alguna CLASE (persona, empleado... etc)
print(isinstance(RafelQuetglas, empleado)) #RafelQuetglas no pertany a EMPLEADO per tant retornarà FALSE