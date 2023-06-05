hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

if hora_inicial == minuto_inicial == hora_final == minuto_final:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
    exit()
# Cálculo da duração em horas
duracao_horas = hora_final - hora_inicial

# Cálculo da duração em minutos
duracao_minutos = minuto_final - minuto_inicial

# Verifica se é necessário ajustar a duração em horas ou minutos
if duracao_minutos < 0:
    duracao_horas -= 1
    duracao_minutos += 60

# Verifica se é necessário ajustar a duração em horas para lidar com casos onde o jogo começou em um dia e terminou no outro
if duracao_horas < 0:
    duracao_horas += 24

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")

