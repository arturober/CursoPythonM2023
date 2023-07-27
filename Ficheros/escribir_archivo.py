def sobrescribir():
    # Si no existe, crea el archivo
    with open('Ficheros/archivos/palabras.txt', 'w') as f:
        for i in range(5):
            palabra = input(f"Dime la palabra {i + 1}: ")
            f.write(palabra + "\n")
        
def anyadir():
    # Si no existe, crea el archivo
    with open('Ficheros/archivos/palabras.txt', 'a') as f:
        for i in range(5):
            palabra = input(f"Dime la palabra {i + 1}: ")
            f.write(palabra + "\n")
            
        
# sobrescribir()
anyadir()
