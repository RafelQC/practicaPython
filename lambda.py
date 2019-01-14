#funcion sencilla que se puede sinplificar con una función lambda
#abajo un ejemplo

'''def area_triangulo(base, altura):

    return (base*altura)/2

triangulo_1=area_triangulo(5,6)
triangulo_2=area_triangulo(7,10)

print(triangulo_1)
print(triangulo_2)


#función lambda que hace lo mismo que la función anterior un poquito más sencillo

area_triangulo=lambda base,altura:(base*altura)/2
print(area_triangulo(7,5))'''

#ejemplo función lambda al cubo
#las dos siguientes elevan al cubo
#al_cubo=lambda numero:numero**3
#al_cubo=lambda numero:pow(numero, 3)
#print(al_cubo(13))


#ejemplo destacar valor

#def destacar_valor(comision):
    #return "¡{}€!".format(comision)

destacar_valor=lambda comision:"¡{}€!".format(comision)

comision_ana=15585

print(destacar_valor(comision_ana))