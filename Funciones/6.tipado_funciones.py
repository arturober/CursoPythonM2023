# Función que ordena una lista y convierte a mayúsculas sus valores
# Al tipar documentamos la función mejor y habilitamos AUTOCOMPLETADO
def ordena_mayus(lista: list[str]) -> list[str]:
    lista = [s.upper() for s in lista]
    lista.sort()
    return lista
    
nombres = ["Pepe", "Juan", "Marta", "Antonio"]
nombres_ordenados = ordena_mayus(nombres)
print(nombres_ordenados)

# DEvuelve el número de veces que aparece una cadena en una lista o tupla
def veces(lista: tuple[str], palabra: str) -> int:
    veces = 0
    for p in lista:
        if p == palabra:
            veces += 1
    return veces

palabras = ("casa", "coche", "moto", "casa", "árbol", "casa")
print(f"casa aparece {veces(palabras, 'casa')} veces") # casa aparece 3 veces
