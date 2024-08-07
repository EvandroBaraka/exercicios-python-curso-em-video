from time import sleep


def contagem(inicio, fim, passo):
	if passo == 0:
		passo = 1
	if inicio > fim:
		f = fim - 1
		if passo > 0:
			p = -passo
		else:
			p = passo
	else:
		if passo < 0:
			p = -1 * passo
		else:
			p = passo
		f = fim + 1

	print('-=' * 15)	
	print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
	for i in range(inicio, f, p):
		print(f'{i}', end=' ', flush=True)
		sleep(0.5)
	print('FIM')
	print()
	

contagem(1, 10, 1)
contagem(10, 0, 2)
print('Agora é sua vez de definir a contagem.')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contagem(a, b, c)
