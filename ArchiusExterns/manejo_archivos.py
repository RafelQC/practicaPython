from io import open #llibreries per operar amb arxius externs

archivo_texto=open("archivo.txt","w") #crear un arxiu extern per a escritura
archivo_texto2=open("archivo2.txt","r") #obrir un arxiu ja creat per a lectura

frase="Estupendo día para estudiar Python \nen miércoles"

archivo_texto.write(frase) #escrivim a l'arxiu les dades desitjades
archivo_texto.close() #tancam l'arxiu per guardar

texto_leido=archivo_texto2.read() #guarda totes les dades llegides a la variable
archivo_texto2.close() #tancam l'arxiu per guardar

print(texto_leido)

#accés per linies

archivo_texto2=open("archivo2.txt","r") #obrir un arxiu ja creat per a lectura

lineas_texto=archivo_texto2.readlines() #guardam tots els arxius de linea en linea en una llista
archivo_texto2.close()

print(lineas_texto) #accedim a tota la llista
print(lineas_texto[0]) #accedim a una posició en concret de la llista

#afegir texte a un arxiu

archivo_texto=open("archivo.txt","a") #obrim l'arxiu per afegir dades

archivo_texto.write("\ncream una línea més yeah")
archivo_texto.close()


