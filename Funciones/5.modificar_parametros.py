def mod_num(n):
    n += 5
    print(f"Función: n vale {n}")
    
n = 24
mod_num(n)
print(f"Main: n vale {n}")
'''
Función: n vale 29 (local)
Main: n vale 24 (global)
'''

def mod_lista(lista):
    # lista = [*lista] # Si generamos una copia de la lista, ya no hay problema
    lista[0] = 99
    print(f"Función: lista -> {lista}")
    
lista = [1, 2, 3, 4]
mod_lista(lista)
print(f"Función: lista -> {lista}")
'''
Función: lista -> [99, 2, 3, 4]
Función: lista -> [99, 2, 3, 4] (ambas variables apuntan a la misma lista)
''' 

