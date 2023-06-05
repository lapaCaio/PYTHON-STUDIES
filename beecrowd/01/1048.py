salario = float(input())

if 0 <= salario <= 400:
    novo_salario = salario * 1.15
    reajuste_ganho = novo_salario - salario
    percentual = 15
elif 400.01 <= salario <= 800:
    novo_salario = salario * 1.12
    reajuste_ganho = novo_salario - salario
    percentual = 12
elif 800.01 <= salario <= 1200:
    novo_salario = salario * 1.10
    reajuste_ganho = novo_salario - salario
    percentual = 10
elif 1200.01 <= salario <= 2000:
    novo_salario = salario * 1.07
    reajuste_ganho = novo_salario - salario
    percentual = 7
else:
    novo_salario = salario * 1.04
    reajuste_ganho = novo_salario - salario
    percentual = 4

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste_ganho:.2f}')
print(f'Em percentual: {int(percentual)} %')
