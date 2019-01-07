# ESCRITURA d'un arxiu en binari

import pickle

lista_nombres=["Pedro", "Ana", "María", "Isabel"]

fichero_binario=open("lista_nombres", "wb") # obrim l'arxiu amb el comando "wb" write binari per escriure en binari

pickle.dump(lista_nombres, fichero_binario) # realitzam l'acció de codificar el llistat de noms i guardarlo a l'arxiu extern

fichero_binario.close() # tancam fixer

del fichero_binario # podem borrar el fixer en memoria, pero no l'extern

# LECTURA d'un arxiu en binari

fichero=open("lista_nombres", "rb") # obrim l'arxiu amb lectura binaria "rb"

lista=pickle.load(fichero) # guardam el contingut de l'arxiu a la variable lista

print(lista)
