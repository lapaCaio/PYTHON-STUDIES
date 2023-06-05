pares = []
i = 0
while i < 5:
    entrada = int(input())
    if entrada % 2 == 0:
        pares.append(entrada)
    i += 1

print(f'{len(pares)} valores pares')

