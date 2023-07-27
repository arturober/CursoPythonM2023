from pathlib import Path

# Vamos a crear el archivo "archivo.txt" dentro de la carpeta "prueba" (si no existe, la creamos)

dir = Path("Ficheros", "prueba") # Relativo al directorio del proyecto (Ficheros/prueba)
if not dir.exists():
    dir.mkdir() # Creamos el directorio

file = dir.joinpath('archivo.txt')
print(file) # Ficheros/prueba/archivo.txt
print(file.absolute()) # /home/arturo/Documentos/CursoPythonM2023/Ficheros/prueba/archivo.txt
with open(file, 'w') as f:
    f.write("Hola")