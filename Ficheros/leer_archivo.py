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
    
# lee_fichero()
# lee_fichero2()
# lee_fichero3()
# lee_fichero4()
suma_numeros()
