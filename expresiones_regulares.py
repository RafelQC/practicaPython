import re

#FUNCION SEARCH
#busca un caracter o una cadena de caracteres dentro de una cadena de caracteres

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de programación sencillo"
#si devuelve un objeto, se ha encontrado, si devuelve NONE no lo ha encontrado
#devuelve NONE
print(re.search("caca",cadena))
#devuelve objeto
print(re.search("regulares",cadena))

texto_buscar="Python"

if re.search(texto_buscar, cadena) is not None:
    print("Hemos encontrado la palabra")
else:
    print("NO hemos encontrado la palabra")


#FUNCION START / END / SPAN /FINDALL

texto_encontrado=re.search(texto_buscar, cadena)

#te devuelve en que posición empieza la palabra buscada o caracter
print(texto_encontrado.start())
#te devuelve en que posicion de la cadena finaliza la palabra o caracter
print(texto_encontrado.end())
#te devuelve la posición que empieza y finaliza la cadena o caracter en una tupla
print(texto_encontrado.span())
#nos devuelve una lista con la palabra buscada, repetida tantas veces como la ha encontrado
print(re.findall(texto_buscar, cadena))
#por tanto si le agregamos la función len() a lo anterior, podemos saber cuantas veces lo ha encontrado
print(len(re.findall(texto_buscar, cadena)))