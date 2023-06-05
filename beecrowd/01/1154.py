entradas = []
condicao = True
while condicao:
    entrada = float(input())
    if entrada < 0:
        condicao = False
        continue
    else:
        entradas.append(entrada)
print(f'{(sum(entradas)/len(entradas)):.2f}')
