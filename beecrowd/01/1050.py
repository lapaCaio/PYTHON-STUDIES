ddd = int(input())

ddds = [61, 71, 11, 21, 32, 19, 27, 31]
cidades = ['Brasilia', 'Salvador', 'Sao Paulo', 'Rio de Janeiro', 'Juiz de Fora', 'Campinas', 'Vitoria', 'Belo Horizonte']

if ddd in ddds:
    idx = ddds.index(ddd)
    print(cidades[idx])
else:
    print('DDD nao cadastrado')
    