inputs = []
i = 0
while i < 3:
    entrada = str(input())
    if entrada:
        inputs.append(entrada.lower())
    else:
        break
    i += 1

if 'vertebrado' in inputs:
    if 'ave' in inputs:
        if 'carnivoro' in inputs:
            print('aguia')
        else:
            print('pomba')
    else:
        if 'onivoro' in inputs:
            print('homem')
        else:
            print('vaca')
else:
    if 'inseto' in inputs:
        if 'hematofago' in inputs:
            print('pulga')
        else:
            print('lagarta')
    else:
        if 'hematofago' in inputs:
            print('sanguessuga')
        else:
            print('minhoca')
