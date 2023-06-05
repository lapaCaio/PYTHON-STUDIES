inputs = []
maior = 0
posicao = 0
for i in range(1, 101):
    entrada = int(input())
    inputs.append(entrada)
    maior = max(inputs)
    posicao = inputs.index(maior) + 1

print(maior)
print(posicao)
