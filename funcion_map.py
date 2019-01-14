#función MAP, devuelve una lista aplicando una función a la lista que le hemos pasado
#devuelve una lista


#filtrar OBJETOS

class Empleado:

    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    #funcion de la clase, cuando imprimimos un objeto(a pelo) esto es lo que nos va a iprimir
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {}€".format(self.nombre, self.cargo, self.salario)

lista_empleados=[
    Empleado("Juan", "Director", 6700),
    Empleado("Ana", "Presidenta", 7500),
    Empleado("Antonio", "Administrativo", 2100),
    Empleado("Sara", "Secretaria", 2150),
    Empleado("Mario", "Botones", 1800),
]

def calculo_comision(empleado):
    if (empleado.salario<=3000):
        #añadimos un 3% al salario de los empleados por comisiones con salario menor a 3000€
        #así que podemos jugar como queramos dentro de la función
        empleado.salario=empleado.salario*1.03
    return empleado
#aplicamos la función map, aplicando la función "calculo_comisión" a toda la lista "lista_empleados"
lista_comision=map(calculo_comision, lista_empleados)

for i in lista_comision:
    print(i)