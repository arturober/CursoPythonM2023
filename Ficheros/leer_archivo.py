import sys

# Lee el contenido de un fichero dentro de un string
def lee_fichero():
    with open("Ficheros/archivos/palabras.txt") as f:
        print(f.read())


# Lee el contenido línea a línea forma clásica (bucle while)
def lee_fichero2():
    with open("Ficheros/archivos/palabras.txt") as f:
        linea = f.readline()
        while linea != "":
            print(linea.strip())
            linea = f.readline()


# Lee el contenido línea a línea (forma Python)
def lee_fichero3():
    with open("Ficheros/archivos/palabras.txt") as f:
        for linea in f:
            print(linea.strip())


# Lee el contenido como una lista de strings (líneas)
def lee_fichero4():
    with open("Ficheros/archivos/palabras.txt") as f:
        lineas = [linea.strip() for linea in f]
        print(lineas)


def suma_numeros():
    with open("Ficheros/archivos/numeros.txt") as f:
        lineas = [int(linea.strip()) for linea in f]
        suma = sum(lineas)
        print(f"Suma: {suma}, Media: {suma/len(lineas)}")


"""    
Ejercicio donde leemos el archivo productos.txt y a partir del mismo
creamos por cada línea un diccionario (ej: {nombre: 'Silla', precio: 34})
Guarda los diccionarios en una lista y muestra su contenido
Además, muestra el producto más barato y la suma de los precios de los productos
"""


# Solución más "avanzada"
def lee_productos():
    with open("Ficheros/archivos/productos.txt") as f:
        tuplas = [linea.split(';') for linea in f]
        productos = [{"nombre": a[0], "precio": int(a[1])} for a in tuplas]

        print(productos)

        productos.sort(key=lambda p: p.get("precio"))  # Ordenamos productos por precio
        print(f"Producto más barato: {productos[0]}")  # El primero será el más barato
        print(
            f"Total precio: {sum(p['precio'] for p in productos)}"
        )  # Extraemos el precio y lo sumamos


# Solución más clásica
def lee_productos2():
    lista = []
    barato = {"nombre": "", "precio": sys.maxsize}
    total = 0
    with open("Ficheros/archivos/productos.txt") as f:
        for linea in f:
            a = linea.strip().split(";")
            lista.append({"nombre": a[0], "precio": int(a[1])})

        for p in lista:
            print(p)
            total += p["precio"]
            if p["precio"] < barato["precio"]:
                barato = p

        print(f"Producto más barato: {barato}")
        print(f"Total precio: {total}")


# lee_fichero()
# lee_fichero2()
# lee_fichero3()
# lee_fichero4()
# suma_numeros()
lee_productos()
lee_productos2()
