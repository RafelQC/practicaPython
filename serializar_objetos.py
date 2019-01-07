import pickle

class Vehiculos():

    def __init__ (self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\n-En marcha:", self.enmarcha,
        "-Acelerando:", self.acelera, "-Frenando:", self.frena)

coche1=Vehiculos("Peugeot", "608")

coche2=Vehiculos("Seat", "Altea")

coche3=Vehiculos("Renault", "Megane")

coches=[coche1, coche2, coche3]

lista_coches=open("losCoches", "wb")

pickle.dump(coches, lista_coches)

lista_coches.close()
del lista_coches

# llegim el fixer

leer_lista=open("losCoches", "rb")

objetos_leidos=pickle.load(leer_lista)
objetos_leidos.close()

objeto_leido1, objeto_leido2, objeto_leido3 = objetos_leidos

objeto_leido1.estado()