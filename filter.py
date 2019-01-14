#funcion filter
#verifica que los elementos de la secuencia cumplen una condición, devolviendo un iterador con los elementos que cumplen dicha condición
#aplica una condición a la lista, que la función devuelva un True
#devuelve una lista

'''def numero_par(num):
    # si el resto es 0
    if num % 2==0:

        return True'''
#numeros=[17,24,35,43,25,20,14,29,24]

#nos devuelve un objeto, por tanto lo transformamos en formato lista "list"
#print(list(filter(numero_par, numeros)))


#lo podemos hacer con la función lambda tambien
numeros=[17,24,35,43,25,20,14,29,24]
print(list(filter(lambda numero_par: numero_par% 2==0, numeros)))

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
    Empleado("Juan", "Director", 75000),
    Empleado("Ana", "Presidenta", 85000),
    Empleado("Antonio", "Administrativo", 25000),
    Empleado("Sara", "Secretaria", 27000),
    Empleado("Mario", "Botones", 21000),
]

salarios_altos=filter(lambda mirar_empleado:mirar_empleado.salario>50000,lista_empleados)


for todos_empleados in salarios_altos:
    print(todos_empleados)