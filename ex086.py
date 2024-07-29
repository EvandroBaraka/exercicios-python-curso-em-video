matriz = [[], [], []]

for linha in range(0, 3):
	for coluna in range(0, 3):
		num = int(input(f'Digite um número para a posição [{linha}] [{coluna}] : '))
		matriz[linha].insert(coluna, num)

print('-=-' * 15)
for l in range(0, 3):
	for c in range(0, 3):
		print(f'[ {matriz[l][c]} ]', end='' )
	print('\n')
	