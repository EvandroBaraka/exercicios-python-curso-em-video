jogador = {'Nome': str(input('Nome do jogador: '))}
jogador['partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
gols = []
totalGols = 0

for i in range(0, jogador['partidas']):
	gols.append(int(input(f'Quantos gols {jogador["Nome"]} marcou na {i + 1}ª partida: ')))
	#totalGols += gols[i]
jogador['gols'] = gols[:]
#jogador['total'] = totalGols
jogador['total'] = sum(gols)
print('-='*35)
print(jogador)
print('-='*35)
for k, v in jogador.items():
	print(f'O campo {k} tem o valor {v}.')
print('-='*35)
print(f'O jogador {jogador["Nome"]} jogou {jogador["partidas"]} partidas.')
for i, v in enumerate(jogador['gols']):
	print(f'  => Na partida {i + 1} ele marcou {v} gols.')
print(f'Foram un total de {jogador["total"]} gols.')