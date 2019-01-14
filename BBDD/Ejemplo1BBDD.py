import sqlite3

#abrimos y creamos la primera base de datos
mi_conexion=sqlite3.connect("Primera_Base")
#iniciamos el cursor
mi_cursor=mi_conexion.cursor()


#invalidamos esta linea de codigo porque solo se debe crear una vez el contenido
#creamos una tabla LLAMADA "PRODUCTOS" con las siguientes características, nombre, precio y sección
#mi_cursor.execute("CREATE TABLE productos (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")



#agregar contenido a las tablas
#mi_cursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 16, 'DEPORTES')" )
#aceptamos los cambios
#mi_conexion.commit()



#insertar varios contenidos a la vez (lote de registros):

#creamos una lista de tuplas para almacenar en la base de datos
varios_productos=[
    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 90, "Cerámica"),
    ("Camión", 20, "Juguetes")
]
#insertar varios contenidos a la vez mediante una lista de tuplas, se ponen tantos interrogantes como valores haya en las tuplas
#mi_cursor.executemany("INSERT INTO productos VALUES(?,?,?)",varios_productos)
#mi_conexion.commit()



#leer información de BBDD:

#utilizar el cursor selccionar todos los registros de "productos"
mi_cursor.execute("SELECT * FROM productos")
#guardar en la lista los valores marcados por el cursor
productos_leidos=mi_cursor.fetchall()

#print(productos_leidos)
for producto in productos_leidos:
    print("El producto es:", producto[0], "y vale", producto[1], "Euros, del apartado", producto[2])



#cerrar base de datos
mi_conexion.close()
