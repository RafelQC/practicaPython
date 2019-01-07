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


class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado=cargar
        if self.cargado:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta NO está cargada"


class Moto(Vehiculos): #se crea una clase heredando todas las propiedades de la clase vehiculos
    h_caballito=""

    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"

    def estado(self):
        super().estado() #se activa el metodo "estado" de la clase padre "vehiculos"
        print(self.hcaballito) #y se le añado otro apartado que es si estamos haciendo un caballito o no
        #print("Marca:", self.marca, "\nModelo:", self.modelo, "\n-En marcha:", self.enmarcha,
        #"-Acelerando:", self.acelera, "-Frenando:", self.frena, "\n", self.hcaballito)


class VElectricos(Vehiculos):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo) #se activa el estado inicial de la clase padre "vehiculos"
        self.autonomia=100 #km

    def cargarEnergia(self):
        self.cargando=True


# herencia múltiple, hereda de vehiculos y de vElectricos
class BicicletaElectrica(VElectricos, Vehiculos):
#IMPORTANTE el orden puesto entre parentesis, pues solo hereda un constructor y será el primero que pongas allí, en este caso "VElectricos"
    pass
