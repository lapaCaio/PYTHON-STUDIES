a, b, c = map(float, input().split())
vetor = [a, b, c]

vetor.sort(reverse=True)
a, b, c = vetor

if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    soma_dos_quadrados = pow(b, 2) + pow(c, 2)

    triangulo_retangulo = pow(a, 2) == soma_dos_quadrados
    triangulo_obtusangulo = pow(a, 2) > soma_dos_quadrados
    triangulo_acutangulo = pow(a, 2) < soma_dos_quadrados
    triangulo_equilatero = a == b == c
    triangulo_isoceles = a == b or a == c or b == c

    if triangulo_retangulo:
        print('TRIANGULO RETANGULO')

    if triangulo_obtusangulo:
        print('TRIANGULO OBTUSANGULO')

    if triangulo_acutangulo:
        print('TRIANGULO ACUTANGULO')

    if triangulo_equilatero:
        print('TRIANGULO EQUILATERO')
    elif triangulo_isoceles:
        print('TRIANGULO ISOSCELES')

