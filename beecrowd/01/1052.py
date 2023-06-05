valor = int(input())

lista_meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
meses = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

idx = lista_meses.index(valor)
print(meses[idx].title())
