#from funciones_matematicas import sumar #ens permet importar només una funció del mòdul "funciones_matematicas" "sumar"
from funciones_matematicas import * #ens permet importar totes les funcions del mòdul "funciones_matematicas"
from modulo_vehiculos import *

sumar(7,4)
restar(5,9)

coche_audi=Vehiculos("Audi", "A7")
coche_audi.estado()