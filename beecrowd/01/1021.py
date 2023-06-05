import math

valor = float(input())

print("NOTAS:")
notas = [100, 50, 20, 10, 5, 2]

for nota in notas:
    quantidade_notas = int(valor // nota)
    print(f"{quantidade_notas} nota(s) de R$ {nota}.00")
    valor = round(valor % nota, 2)

print("MOEDAS:")
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

for moeda in moedas:
    quantidade_moedas = math.floor(valor / moeda)
    print(f"{quantidade_moedas} moeda(s) de R$ {moeda:.2f}")
    valor = round(valor % moeda, 2)
