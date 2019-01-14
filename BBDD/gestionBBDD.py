import sqlite3

#mi_conexion=sqlite3.connect("gestion_productos")
#mi_cursor=mi_conexion.cursor()

#creamos una tabla con una clave para cada "articulo" o para cada cosa que deseemos guardar en la BBDD "PRIMARY KEY"
#este valor no se podrá repetir en la BBDD o nos dará error
#mi_cursor.execute('''
    #CREATE TABLE PRODUCTOS (
    #CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    #NOMBRE_ARTICULO VARCHAR(50),
    #STOCK_ARTICULO INTEGER,
    #SECCION_ARTICULO VARCHAR(20),
    #PRECIO_ARTICULO INTEGER)
#''')

#mis_productos=[
    #("AR01", "pelota adidas", 15, "deportes", 30),
    #("AR02", "jarra verde", 5, "decoración", 47),
    #("AR03", "foam roller", 10, "deportes", 17),
    #("AR04", "martillo", 7, "ferretería", 45),
    #("AR05", "pantalon beix", 15, "moda", 30)
#]

#mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?,?,?)", mis_productos)

#mi_conexion.commit()
#mi_conexion.close()



#AUTO gestion del numero clave con un incremento automático

#mi_conexion=sqlite3.connect("AUTOgestion_productos")
#mi_cursor=mi_conexion.cursor()

#creamos una tabla con un paramatro "ID" normalizado y un AUTOINCREMENT que nos irá dando cada vez un valor mayor
#UNIQUE: no se puede repetir el nombre del campo, por ejemplo DNI, etc
#mi_cursor.execute('''
    #CREATE TABLE PRODUCTOS (
    #ID INTEGER PRIMARY KEY AUTOINCREMENT,
    #NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    #STOCK INTEGER,
    #SECCION VARCHAR(20),
    #PRECIO INTEGER)
#''')


#en este apartado debemos obviar el apartado ID que se va creando de manera automatica por el AUTOINCREMENT del 1 al infinito
#mis_productos=[
    #("pelota adidas", 15, "deportes", 30),
    #("jarra verde", 5, "decoración", 47),
    #("foam roller", 10, "deportes", 17),
    #("martillo", 7, "ferretería", 45),
    #("pantalon beix", 15, "moda", 30),
    #("colchon biscolatex", 3, "casa", 500)
#]

#en el lugar del interrogante donde perteneceria el ID autoincrementable ponemos un "NULL"
#mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?,?)",mis_productos)

#mi_conexion.commit()
#mi_conexion.close()


#LECTURA de determinados datos

mi_conexion=sqlite3.connect("AUTOgestion_productos")
mi_cursor=mi_conexion.cursor()

#seleccionar - ponemos el cursor en los datos que queremos mirar
mi_cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='deportes'")

productos=mi_cursor.fetchall()
for p in productos:
    print(p)

mi_conexion.commit()
mi_conexion.close()

#ACTUALIZAR los datos

mi_conexion=sqlite3.connect("AUTOgestion_productos")
mi_cursor=mi_conexion.cursor()

#modificamos el valor del dato seleccionado
mi_cursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pantalon beix'")


mi_conexion.commit()
mi_conexion.close()


#BORRAR datos de la BBDD

mi_conexion=sqlite3.connect("AUTOgestion_productos")
mi_cursor=mi_conexion.cursor()

#borramos la tupla seleccionada por ID, o por algun nombre UNIQUE (para asegurar el tiro ;D)
mi_cursor.execute("DELETE FROM PRODUCTOS WHERE ID=6")


mi_conexion.commit()
mi_conexion.close()