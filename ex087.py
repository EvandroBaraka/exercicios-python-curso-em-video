matriz = [[], [], []]
pares = coluna3 = 0

for linha in range(0, 3):
	for coluna in range(0, 3):
		num = int(input(f'Digite um número para a posição [{linha}] [{coluna}] : '))
		matriz[linha].insert(coluna, num)
		if num % 2 == 0:
			pares += num
coluna3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
print('-=-' * 15)
for l in range(0, 3):
	for c in range(0, 3):
		print(f'[ {matriz[l][c]} ]', end='' )
	print('\n')
print('-=-' * 15)
print(f'A soma dos números pares é {pares}')
print(f'A soma dos valores da terceira coluna é {coluna3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')