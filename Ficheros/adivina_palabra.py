def lee_fichero():
    with open("Ficheros/archivos/palabras.txt") as f:
        return [linea.strip() for linea in f]
    
def anyade_palabra(palabra):
    with open("Ficheros/archivos/palabras.txt", 'a') as f:
        f.write(palabra + "\n")
        
lineas = lee_fichero()
palabra = input("Adivina una palabra: ")
if palabra in lineas:
    print(f"Has acertado!, la palabra {palabra} está")
else:
    print(f"Lo siento..., la palabra {palabra} no está. La añadimos...")
    anyade_palabra(palabra)
    