from random import randint

tupla = (randint(1,10), randint(1,10),
		 randint(1,10), randint(1,10),
		 randint(1,10))

print('Os números sorteados foram: ', end='')
for c in tupla:
	print(c, end=' ')
print(f'\nO maior número é o {max(tupla)}')
print(f'O menor número é o {min(tupla)}')