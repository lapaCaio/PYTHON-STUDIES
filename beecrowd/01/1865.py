n = int(input())

for i in range(n):
    nome, forca = input().split()
    nome = str(nome).lower().strip()
    if nome == 'thor':
        print('Y')
    else:
        print('N')
