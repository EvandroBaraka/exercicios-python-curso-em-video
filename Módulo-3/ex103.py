def ficha(nome, gols):
	if nome == '' or nome.isspace():
		nome = '<Desconhecido>'
	if gols == '' or nome.isspace():
		gols = 0
	print(f'O jogador {nome} marcou {gols} nesta competição.')
	
	
jogador = str(input('Digite o nome: '))
gols = str(input('Quantos gols marcou: '))
print('-' * 30)
ficha(jogador, gols)