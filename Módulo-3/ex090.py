aluno = {}

aluno['nome'] = str(input('Nome do aluno: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] >= 7:
	aluno['situação'] = 'APROVADO'
elif aluno['média'] >= 5:
	aluno['situação'] = 'RECUPERAÇÃO'
else:
	aluno['situação'] = 'REPROVADO'

print(f'O nome é {aluno["nome"]}.')
print(f'A média é {aluno["média"]}.')
print(f'A situação é {aluno["situação"]}')
