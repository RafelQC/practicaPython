import re
lista_nombres=['Ana gomez','Maria Martín','Sandra López','Santiago Martín','Sandra Oviedo','Ana Izquierdo','Maria Garcia']
lista_url=['ftp://pildorasinformaticas.com',
           'http://whatsapp.com',
           'http://meneame.es',
           'ftp://google.es',
           'http://informaticaenespaña.com']
lista_personas=['hombres',
                'mujeres',
                'mascotas',
                'niños',
                'niñas',
                'camion',
                'camión']

for i in lista_nombres:
    #el simbolo (^) hace referencia a si la cadena empieza por "Sandra"
    #devuelve una lista con el string incial encontrado, puede ser una letra o una palabra
    if re.findall('^Sandra', i):
        print(i)

for i in lista_url:
    #el simbolo ($) hace referencia a si la cadena acaba por "Martín"
    if re.findall('.es$', i):
        print(i)

for i in lista_url:
    #el simbolo ([]) nos busca si contiene los caracteres indicado ¡SIN IMPORTAR EL ORDEN!
    if re.findall('[ñ]', i):
        print(i)

for i in lista_personas:
    #el simbolo ([]) intercalado en un string buscara las combinaciones que busques
    if re.findall('niñ[ao]s', i):
        print(i)
for i in lista_personas:
    #ejemplo para busquedas con o sin acento
    if re.findall('cami[oó]n', i):
        print(i)

#RANGO de caracteres

lista_propios=['Ana',
               'Pedro',
               'María',
               'Rosa',
               'Sandra',
               'Celia']

for i in lista_propios:
    #que contenga uno de los caracteres comprendidos entre el rango O-T del abecedario
    if re.findall('[o-t]', i):
        print(i)
for i in lista_propios:
    #que empiece por uno de los caracteres comprendidos entre el rango O-T del abecedario
    if re.findall('^[O-T]', i):
        print(i)
for i in lista_propios:
    #que finalice por uno de los caracteres comprendidos entre el rango O-T del abecedario
    if re.findall('[o-t]$', i):
        print(i)

lista_codigos=['Ma1','Se1','Ma2','Ba1','Ma3','Va1','Va2','Ma4']
lista_codigos2=['Ma1','Se1','Ma2','Ba1','Ma3','Va1','Va2','Ma4','MaA','Ma5','MaB','MaC']
lista_codigos3=['Ma.1','Se1','Ma2','Ba1','Ma:3','Va1','Va2','Ma4','MaA','Ma.5','MaB','Ma:C']

for i in lista_codigos:
    #nos devuelve aquellos rangos comprendidos y compuestos con Ma
    if re.findall('Ma[0-3]', i):
        print("*",i)

for i in lista_codigos:
    #nos devuelve aquellos rangos que no son los establecidos (seria la negada de la de arriba)
    if re.findall('Ma[^0-3]', i):
        print("^",i)

for i in lista_codigos2:
    #imprime tango el rango (0-3) como el (A-B)
    if re.findall('Ma[0-3A-B]', i):
        print("-",i)
for i in lista_codigos3:
    #imprime los que contengan dichos caracteres
    if re.findall('Ma[.:]', i):
        print(".",i)
