N = int(input())
in_vet = []
out_vet = []
i = 0
while i < N:
    entrada = float(input())
    if 10 <= entrada <= 20:
        in_vet.append(entrada)
    else:
        out_vet.append(entrada)
    i += 1
print(str(len(in_vet)) + " in")
print(str(len(out_vet)) + " out")
