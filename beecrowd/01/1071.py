valores = []
i = 0
while i < 2:
    valor = int(input())
    valores.append(valor)
    i += 1

valores.sort()
impares = [x for x in range(valores[0] + 1, valores[1]) if x % 2 != 0]

print(sum(impares))
