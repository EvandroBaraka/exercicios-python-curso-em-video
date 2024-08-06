jogador = dict()
listaJogadores = []

while True:
	print('-' * 35)
	jogador.clear()
	jogador = {'Nome': str(input('Nome do jogador: '))}
	jogador['partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
	gols = []
	totalGols = 0
	
	for i in range(0, jogador['partidas']):
		gols.append(int(input(f'Quantos gols na {i + 1}ª partida: ')))
		totalGols += gols[i]
	jogador['gols'] = gols[:]
	jogador['total'] = totalGols
	listaJogadores.append(jogador.copy())
	while True:
		continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
		if continuar in 'SN':
			break
		print('ERRO. Digite apenas S ou N...')
	if continuar == 'N':
		break

print('-=' * 25)
print(f'{"Cod.":<5} {"Nome":<15} {"Gols":<20} {"Total":<5}')
for i, v in enumerate(listaJogadores):
	print(f'{i + 1:^5} {v["Nome"]:<15} {str(v["gols"]):<20} {v["total"]:<5}')

while True:
	while True:
		print('-' * 50)
		opçao = int(input('Mostrar dados de qual jogador (999 encerra): ')) - 1
		if opçao < len(listaJogadores) or opçao == 998:
			break
		else:
			print('Opção inválida. Cód de jogador inexistente...')
	if opçao == 998:
		break
	print(f'-- LEVANTAMENTO DO JOGADOR {listaJogadores[opçao]["Nome"]}')
	for c in range(0, listaJogadores[opçao]['partidas']):
		print(f'   Na {c + 1}ª partida marcou {listaJogadores[opçao]["gols"][c]} gols.')
print('   <<<ENCERRANDO>>>')
print()
print()
