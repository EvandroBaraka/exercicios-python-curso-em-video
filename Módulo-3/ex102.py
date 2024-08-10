def fatorial(n, show=False):
	"""
	-> Calcula o fatorial de um número
	:param n: o número a ser calculado
	:param show: (opcional) mostra ou não o cálculo.
	:return n: o Fatorial de um número n	
	"""
	fat = 1
	if show:
		print(f'{n}! = ', end='')
		for c in range(n, 0, -1):
			fat *= c
			if c > 1:
				print(f'{c} ', end='x ')
			else:
				print(f'{c} ', end='= ')
	else:
		for c in range(n, 0, -1):
			fat *= c
	return fat


num = int(input('Digite um número para ver seu fatorial: '))
resp = ''
while True:
	resp = str(input('Deseja exibir o cálculo [S/N]?  ')).upper().strip()[0]
	if resp not in 'SN':
		print('Opção inválida')
	else:
		if resp == 'S':
			resp = True
		else:
			resp = False
		break
print('-' * 30)
print(fatorial(num, resp))
