codigo, quantidade = map(int, input().split())

codigos = [1, 2, 3, 4, 5]
quantidade = float(quantidade)

if codigo in codigos:
    if codigo == 1:
        print(f'Total: R$ {quantidade*4.00:.2f}')
    elif codigo == 2:
        print(f'Total: R$ {quantidade*4.50:.2f}')
    elif codigo == 3:
        print(f'Total: R$ {quantidade*5.00:.2f}')
    elif codigo == 4:
        print(f'Total: R$ {quantidade*2.00:.2f}')
    elif codigo == 5:
        print(f'Total: R$ {quantidade*1.50:.2f}')
