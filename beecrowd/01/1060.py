inputs = []
i = 0
while i < 6:
    entrada = float(input())
    inputs.append(entrada)
    i += 1

valores_positivos = [x for x in inputs if x > 0]
print(f'{len(valores_positivos)} valores positivos')
