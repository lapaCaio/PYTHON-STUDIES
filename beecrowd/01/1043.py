A, B, C = map(float, input().split())
vet = [A, B, C]
vet.sort()
Azin, Bzin, Czin = vet

if (Azin + Bzin) > Czin:
    print(f'Perimetro = {(Azin + Bzin + Czin):.1f}')
else:
    area = ((A + B) * C)/2
    print(f'Area = {area:.1f}')
