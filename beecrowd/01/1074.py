pares = []
impares = []
maior = []
menor = []
inputs = []
N = int(input())
i = 0
entrada = 0
for i in range(N):
    entrada = int(input())
    inputs.append(entrada)
    if entrada == 0:
        continue
    if entrada % 2 == 0:
        pares.append(entrada)
    else:
        impares.append(entrada)
    if entrada > 0:
        maior.append(entrada)
    elif entrada < 0:
        menor.append(entrada)

for entrada in inputs:
    if entrada in pares and entrada in maior:
        print('EVEN POSITIVE')
    elif entrada in pares and entrada in menor:
        print('EVEN NEGATIVE')
    elif entrada in impares and entrada in maior:
        print('ODD POSITIVE')
    elif entrada in impares and entrada in menor:
        print('ODD NEGATIVE')
    else:
        print('NULL')
