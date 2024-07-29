tupla = ('zero', 'um', 'dois', 'três', 'quatro',
		  'cinco', 'seis', 'sete', 'oito', 'nove',
		    'dez', 'onze', 'doze', 'treze', 'quatorze', 
			'quinze', 'dezesseis', 'dezessete', 
			'dezoito', 'dezenove', 'vinte')
while True:
	num = 30
	while num not in range(0, 21):
		num = int(input('Digite um número de 0 a 20: '))
		if num > 20 or num < 0:
			print('Número inválido')
	print(f'Você digitou o número {tupla[num]}')
	print('=' * 30)
	continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
	while continuar not in 'SN':
		print('Opção inválida.')
		continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
	if continuar == 'N':
		break
