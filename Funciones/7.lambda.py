# Función normal
def suma(n1, n2):
    return n1 + n2


# Funcion lambda
resta = lambda n1, n2: n1 - n2

print(type(suma))  # <class 'function'>
print(type(resta))  # <class 'function'>

print(suma(5, 3))
print(resta(5, 3))


def operar(f, n1: int, n2: int) -> int:
    return f(n1, n2)


print(operar(suma, 4, 5))  # 9
print(operar(resta, 4, 5))  # -1
print(operar(lambda n1, n2: n1 * n2, 4, 5))  # 20

# Utilizar lambda para ordenar por longitud una lista de cadenas
nombres = ["Pepe", "Ana", "Marcos", "Anastasia", "Pedro"]
nombres.sort(key=lambda s: len(s))
print(nombres)

personas = [
    {"nombre": "Pepe", "edad": 23},
    {"nombre": "Ana", "edad": 65},
    {"nombre": "María", "edad": 15},
    {"nombre": "Alberto", "edad": 35},
]

#Ordenamos por nombre
personas.sort(key = lambda s : s["nombre"])
print(personas)

#Ordenamos por edad
personas.sort(key = lambda s : s["edad"])
print(personas)