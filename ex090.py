aluno = {}

aluno['nome'] = str(input('Nome do aluno: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

print(f'O nome é {aluno["nome"]}.')
print(f'A média é {aluno["média"]}.')
if aluno['média'] >= 7:
	print('A situação é APROVADO.')
else:
	print('A situação é REPROVADO.')