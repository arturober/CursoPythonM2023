def info_punto(x, y):
    print(f"El punto está en [{x}, {y}]")
    
info_punto(2, 5)

punto = (4, 7)
info_punto(punto[0], punto[1]) # El punto está en [4, 7]
info_punto(*punto) # Desagrupamos la tupla -> El punto está en [4, 7]

punto2 = { "y": 9, "x": 6}
info_punto(punto2["x"], punto2["y"]) # El punto está en [6, 9]
info_punto(**punto2) # El punto está en [6, 9]

# Concatenar listas y valores
palabras = ("casa", "coche", "árbol")
palabras2 = ("manzana", "pera", "plátano")
palabras3 = (*palabras, "fresa", *palabras2)
print(palabras3) #  ('casa', 'coche', 'árbol', 'fresa', 'manzana', 'pera', 'plátano')

# Concatenar diccionarios
diccionario1 = { "a": 4, "b": 9}
diccionario2 = { "c": 7, "d": 14}
diccionario3 = {**diccionario1, **diccionario2}
print(diccionario3) # {'a': 88, 'b': 9, 'c': 7, 'd': 14}

