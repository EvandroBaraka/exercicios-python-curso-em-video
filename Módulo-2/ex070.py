print('-' * 40)
print('{:^40}'.format('LOJA PASSAIA'))
print('-' * 40)
total = 0
produtos = 0
nome = ''
menor = 0
while True:
	produto = str(input('Nome do produto: ')).strip()
	preço = float(input('Preço do produto: R$ '))
	total += preço
	if preço > 1000:
		produtos += 1
	if nome == '':
		nome = produto
		menor = preço
	if preço < menor:
		nome = produto
		menor = preço
	continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
	while continuar not in 'SN':
		print('OPÇÃO INVÁLIDA')
		continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
	if continuar == 'N':
		print('=' * 25)
		break
	print('=' * 25)
print(f'O total das compras foi de R${total:.2f}')
print(f'{produtos} produtos custaram mais de R$1000.00')
print(f'O produto mais barato foi {nome}, que custou R${menor:.2f}')