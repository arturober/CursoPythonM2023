numeros = (23, 14, 67, 9, 8, 10, 11)

# Genera una lista con los números de la original duplicados
transformados = list(map(lambda n: n * 2, numeros))
print(transformados)  # [46, 28, 134, 18, 16, 20, 22]

# Lo mismo usando listas por comprensión
transformados2 = [n * 2 for n in numeros]
print(transformados2)  # [46, 28, 134, 18, 16, 20, 22]

###########################################################

# Genera una lista con los números pares de la original divididos entre 2
transformados3 = list(map(lambda n: int(n / 2), filter(lambda n: n % 2 == 0, numeros)))
print(transformados3)  # [7, 4, 5]

# Con listas por comprension
transformados4 = [int(n / 2) for n in numeros if n % 2 == 0]
print(transformados4)  # [7, 4, 5]

