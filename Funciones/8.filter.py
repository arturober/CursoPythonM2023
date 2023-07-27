numeros = (23, 14, 67, 9, 8, 10, 11)

# Crea una lista/tupla con los números pares
pares = list(filter(lambda n: n % 2 == 0, numeros))
print(pares)

# Igual con listas por comprension
pares2 = [n for n in numeros if n % 2 == 0]
print(pares2)

# Igual con código clásico
pares3 = []
for n in numeros:
    if n % 2 == 0:
        pares3.append(n)
print(pares3)
