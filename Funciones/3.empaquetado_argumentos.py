def suma(*numeros):
    print(sum(numeros))
    
suma(3, 4, 5, 2, 7) # 21
suma(3, 4, 5) # 12
suma(6) # 6
suma() # 0

def info_persona(nombre, *aficiones):
    print(f"Las aficiones de {nombre} son: {', '.join(aficiones)}")
    
info_persona("Pedro", "Viajar", "Tenis", "Dormir")
# Las aficiones de Pedro son: Viajar, Tenis, Dormir
info_persona("Pedro") # Las aficiones de Pedro son:

print ("****************************************")

def agrupa(**valores):
    print(valores)

agrupa(nombre = "Pepito", edad = 46, correo = "pepito@gmail.com")
# {'nombre': 'Pepito', 'edad': 46, 'correo': 'pepito@gmail.com'}

def agrupa(*posicionales, **nominales):
    print(f"Posicionales: {posicionales}, nominales: {nominales}")

agrupa(34, 65, 100, edad = 24, nombre = "Juan")
# Posicionales: (34, 65, 100), nominales: {'edad': 24, 'nombre': 'Juan'}