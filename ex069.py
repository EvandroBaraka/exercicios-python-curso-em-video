pessoas18 = 0
homens = 0
mulheres20 = 0
continuar = 'S'
while continuar == 'S':
	print('-' * 30)
	print('{:-^30}'.format('CADASTRE UMA PESSOA'))
	print('-' * 30)
	idade = int(input('Idade: '))
	sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
	print('-' * 30)
	
	while sexo not in 'MF':
		sexo = str(input('Sexo: [M/F] '))
		
	if idade > 18:
		pessoas18 += 1
	if sexo == 'M':
		homens += 1
	if sexo == 'F' and idade <= 20:
		mulheres20 += 1
	continuar = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
	while continuar not in 'SN':
		continuar = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
		
print(f'Foram cadastradas {pessoas18} pessoas com mais de 18 anos.')
print(f'Tivemos {homens} homens cadastrados.')
print(f'Tivemos {mulheres20} mulheres com menos de 20 anos cadastradas.')