from io import open

archivo_texto3=open("archivo.txt","r")

print(archivo_texto3.read()) #python utilitza punteros, una vegada llegit tot l'arxiu el punter es queda al final
print(archivo_texto3.read()) #si tornam a utilitzar directament aquesta opció, no pasarà res doncs el punter estará al final de l'arxiu inicialment i no llegirà res

archivo_texto3.seek(0) #si tornam a posicionar el punter a l'inici de l'arxiu, podrem tornar a llegir-lo

print("\n", archivo_texto3.read())

archivo_texto3.seek(36) #també el podem posicionar al lloc on desitgem començar a llegir

print("\n", archivo_texto3.read())
archivo_texto3.seek(0)

print("\n", archivo_texto3.read(35)) #aquesta opció ens fa llegir desde la posició 0 fins la posició expecificada (35)
archivo_texto3.seek(0)

archivo_texto3.seek(int(len(archivo_texto3.read())/2)) #situam el punter just a la meitat del texte

print("Imprimim a partir de la meitat del texte:\n", archivo_texto3.read())
archivo_texto3.seek(0)

archivo_texto3.seek(len(archivo_texto3.readline())) #situam el punter just a la meitat del texte

print("Imprimim a partir de la primera linea:\n", archivo_texto3.read())
archivo_texto3.seek(0)

archivo_texto3.close()

archivo_texto4=open("archivo.txt", "r+") #podem obrir l'arxiu tant com lectura com escritura

#archivo_texto4.write("Comienzo texto")

print("\n", archivo_texto4.readlines())
archivo_texto4.seek(0)

lista_texto=archivo_texto4.readlines()
print(lista_texto)

lista_texto[1]="Esta linea ha sido añadida mediante el uso de listas\n" #sobresceibim    un texte dins la llista guardada de l'arxiu
print(lista_texto)

archivo_texto4.seek(0)
archivo_texto4.writelines(lista_texto)

archivo_texto4.close()
