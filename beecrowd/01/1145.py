x, y = map(int, input().split())
texto = ' '
for i in range(1, y + 1):
    texto = texto + str(i) + ' '
    if i % x == 0:
        texto = texto.strip()
        print(texto)
        texto = ' '
