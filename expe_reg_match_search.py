import re

nombre1="sandra López"
nombre2="Jara Gómez"
nombre3="Lara López"

cadena1="Jara López"
cadena2="546546546"
cadena3="a54654654"

codigo1="dwidhwuifhbnbflw71nfbijhbhbwlibfbbdfahdf"
codigo2="wdfjqokwd71klplksmkfmkjmfolñomofcnñmnfconjmjcvookjvcnwnjjnofivoijvfokjfñnjmn"
codigo3="fefjio fjioewfjoij f iofjiowefjio  ifojwo fj9390 i j 39 39k ok 30 i"

#MATCH, busca coincidencias al comienzo de una cadena de texto
#re.IGNORECASE ignora mayusculas o minusculas
if re.match("Sandra", nombre1, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No hemos encontrado el nombre")

if re.match(".ara", nombre2, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No hemos encontrado el nombre")

if re.match(".ara", nombre3, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No hemos encontrado el nombre")

#\d con match si la cadena comienza por un numero
if re.match("\d", cadena3):
    print("Hemos encontrado el número")
else:
    print("No hemos encontrado el número")

#SEARCH no busca al principio, si no que busca en cualquier punto
if re.search("López", nombre3, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No hemos encontrado el nombre")

if re.search("71", codigo2):
    print("Hemos encontrado el código")
else:
    print("No hemos encontrado el código")