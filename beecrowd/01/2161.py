n = int(input())
aux = 0.00
while n:
    aux += 6
    aux = 1.0 / aux
    n -= 1
print("%.10f" % (aux + 3))
