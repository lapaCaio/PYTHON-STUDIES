pares = []
impares = []
maior = []
menor = []

i = 0
while i < 5:
    entrada = int(input())
    if entrada % 2 == 0:
        pares.append(entrada)
    else:
        impares.append(entrada)
    if entrada > 0:
        maior.append(entrada)
    elif entrada < 0:
        menor.append(entrada)
    i += 1

print(f'{len(pares)} valor(es) par(es)')
print(f'{len(impares)} valor(es) impar(es)')
print(f'{len(maior)} valor(es) positivo(s)')
print(f'{len(menor)} valor(es) negativo(s)')



