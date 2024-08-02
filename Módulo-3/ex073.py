times = ('Botafogo', 'Palmeiras', 'Flamengo', 'São Paulo', 'Bahia', 'Cruzeiro', 'Fortaleza', 'Athletico-PR', 'Vasco da Gama', 'Red Bull Bragantino', 'Internacional', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Santos', 'Corinthians', 'Cuiabá', 'Goiás', 'Coritiba', 'Juventude' )

print('=*=' *20)
print('{:^60}'.format('CAMPEONATO BRASILEIRO'))
print('=*=' *20)

print(f'A tabela do Campeonato Brasileiro é: {times}')
print('=' * 40)

print(f'Os cinco primeiros colocados são: {times[0:5]}')
print('=' * 40)

print(f'Os últimos quatro colocados são: {times[-4:]}')
print('=' * 40)

print(f'Os participantes em ordem alfabetica são: {sorted(times)}')
print('=' * 40)

print(f'O time do Grêmio está na {times.index("Grêmio") + 1}ª posição.')