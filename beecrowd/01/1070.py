x = int(input())
i = x
contador_impares = 0

while True:
    if i % 2 == 1:
        print(i)
        contador_impares += 1
    i += 1
    if contador_impares == 6:
        exit()
